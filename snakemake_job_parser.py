import re
from dateutil.parser import parse

def get_ass_from_input(start_rule):
    rule = start_rule[1]
    if rule == 'braker2':
        return start_rule[2].split('/')[0].strip()
    elif rule == 'diamond':
        return start_rule[2].split(',')[1].split('/')[0].strip()


def log2dic(snakemake_log) -> dict:
    start_rule_re = re.compile(r"\[(?P<start_time>.+)\]\nrule (?P<rule>\w+):\n    input:(?P<input>.+)\n    output: .+\n    jobid: (?P<jobid>\d+)\n    wildcards:.+\n    (threads: \d+\n    )?resources: .+\n")
    finish_rule_re = re.compile(r"\[(.+)\]\nFinished job (\d+)")
    error_rule_re = re.compile(r"\[(.+)\]\nError in rule (.+):\n    jobid: (\d+)\n    output: (.+)\n    shell:\n(.+\n.+)")

    syntax_error_re = re.compile(r"SyntaxError in .+\ninvalid syntax")
    name_error_re = re.compile(r"NameError in .+\nname")

    snakemake_str = ''
    with open(snakemake_log) as smlog:
        for line in smlog:
            snakemake_str += line
    
    if syntax_error_re.findall(snakemake_str):
        return "SyntaxError"
    if name_error_re.findall(snakemake_str):
        return "NameError"
    

    start_rule_lis = start_rule_re.findall(snakemake_str)
    finish_rule_lis = finish_rule_re.findall(snakemake_str)

    complete_rule = None
    for finish_rule in finish_rule_lis:
        # ('Sun Mar  6 09:10:38 2022', '13')
        if finish_rule[1] == '0':
            complete_rule = finish_rule
            finish_rule_lis.remove(finish_rule)

    error_rule_lis = error_rule_re.findall(snakemake_str)

    job_dic = {}
    for start_rule in start_rule_lis:
        start_date = start_rule[0]
        start_date_parse = parse(start_date)

        rule = start_rule[1]
        input_ass = get_ass_from_input(start_rule)
        jobid = start_rule[3]
        job_dic[jobid] = (rule, input_ass, start_date_parse)
        # print(start_date, rule, input_ass, jobid)

    for finish_rule in finish_rule_lis:
        finish_date = finish_rule[0]
        finish_date_parse = parse(finish_date)
        jobid = finish_rule[1]
        job_dic[jobid] = (job_dic[jobid] + (finish_date_parse, ))

    for error_rule in error_rule_lis:
        error_date = error_rule[0]
        error_date_parse = parse(error_date)
        jobid = error_rule[2]
        job_dic.pop(jobid)
        # print(error_rule)

    return job_dic
    # job_dic
    # jobid : rule input_ass, start_date_parse, finish_date_parse 

    # for job, info in job_dic.items():
    #     running_time = str((info[3] - info[2]))
    #     print(info[0] + ": " + job + info[1] + " " + running_time)

def get_braker2_finished_lis(snakemake_log):
    fin_lis = []
    job_dic = log2dic(snakemake_log)
    info_lis =  job_dic.values()
    for info in info_lis:
        fin_lis.append(info[1].strip())
    return fin_lis

def main():
    dic = log2dic(r'C:\Users\lr201\code\gene_prediction_pipeline\test\2022-03-04T193108.332047.snakemake.log')
    print(len(dic))
    for jobid, info in dic.items():
        print(jobid, info)

if __name__ == '__main__':
    main()

