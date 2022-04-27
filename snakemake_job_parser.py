import re
from dateutil.parser import parse

def get_ass_from_input(start_rule):
    # get correct ass by input in different rules
    rule = start_rule[1]
    if rule in ('braker2', 'interproscan', 'star_remove'):
        return start_rule[2].split('/')[0].strip()
    elif rule == 'diamond':
        return start_rule[2].split(',')[1].split('/')[0].strip()
    # Rfam
    # trnascan-se

def log2dic(snakemake_log) -> dict:
    snakemake_str = ''
    with open(snakemake_log) as smlog:
        for line in smlog:
            snakemake_str += line

    start_rule_re = re.compile(r"\[(?P<start_time>.+)\]\nrule (?P<rule>\w+):\n    input:(?P<input>.+)\n    output: .+\n    jobid: (?P<jobid>\d+)\n    wildcards:.+\n    (threads: \d+\n    )?resources: .+\n")
    finish_rule_re = re.compile(r"\[(.+)\]\nFinished job (\d+)")
    error_rule_re = re.compile(r"\[(.+)\]\nError in rule (.+):\n    jobid: (\d+)\n    output: (.+)\n    shell:\n(.+\n.+)")

    syntax_error_re = re.compile(r"SyntaxError in .+\ninvalid syntax")
    name_error_re = re.compile(r"NameError in .+\nname")
    missing_input_error_re = re.compile(r"MissingInputException in .+\nMissing input")
    wildcard_error_re = re.compile(r"WildcardError in .+\nWildcards in")

    if syntax_error_re.findall(snakemake_str):
        return "SyntaxError"
    if name_error_re.findall(snakemake_str):
        return "NameError"
    if missing_input_error_re.findall(snakemake_str):
        return "MissingInputError"
    if wildcard_error_re.findall(snakemake_str):
        return "WildcardError"
    

    start_rule_lis = start_rule_re.findall(snakemake_str)
    finish_rule_lis = finish_rule_re.findall(snakemake_str)

    # handling when snakemake does all jobs correctly
    complete_rule = None
    for finish_rule in finish_rule_lis:
        # finish_rule: (time, jobid)
        if finish_rule[1] == '0':
            complete_rule = finish_rule
            # total jobid 0 does not have finish rule, remove it to avoid catched by error rule
            finish_rule_lis.remove(finish_rule)

    error_rule_lis = error_rule_re.findall(snakemake_str)

    job_dic = {}
    for start_rule in start_rule_lis:
        # start_rule: (strat_time, rule, ass, jobid, thread)
        start_date = start_rule[0]
        start_date_parse = parse(start_date)

        rule = start_rule[1]
        input_ass = get_ass_from_input(start_rule)
        jobid = start_rule[3]
        job_dic[jobid] = (rule, input_ass, start_date_parse)

    for finish_rule in finish_rule_lis:
        # finish_rule: (time, jobid)
        finish_date = finish_rule[0]
        finish_date_parse = parse(finish_date)
        jobid = finish_rule[1]
        job_dic[jobid] = (job_dic[jobid] + (finish_date_parse, ))

    for error_rule in error_rule_lis:
        # error_rule: (time, rule, jobid, output, shell)
        error_date = error_rule[0]
        error_date_parse = parse(error_date)
        jobid = error_rule[2]
        job_dic.pop(jobid)

    return job_dic
    # job_dic
    # jobid : rule input_ass, start_date_parse, finish_date_parse 

    # for job, info in job_dic.items():
    #     running_time = str((info[3] - info[2]))
    #     print(info[0] + ": " + job + info[1] + " " + running_time)



def main():
    dic = log2dic(r'C:\Users\lr201\code\gene_prediction_pipeline\test\2022-03-04T193108.332047.snakemake.log')
    print(len(dic))
    for jobid, info in dic.items():
        print(jobid, info)

if __name__ == '__main__':
    main()

