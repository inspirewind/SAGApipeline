import re
from dateutil.parser import parse

def log2dic(snakemake_log) -> dict:
    start_rule_re = re.compile(r"\[(?P<start_time>.+)\]\nrule (?P<rule>\w+):\n    input:(?P<input>.+)\n    output: .+\n    jobid: (?P<jobid>\d+)\n    wildcards:.+\n    (threads: \d+\n    )?resources: .+\n")
    finish_rule_re = re.compile(r"\[(.+)\]\nFinished job (\d+)")
    error_rule_re = re.compile(r"\[(.+)\]\nError in rule (.+):\n    jobid: (\d+)\n    output: (.+)\n    shell:\n(.+\n.+)")

    snakemake_str = ''
    with open(snakemake_log) as smlog:
        for line in smlog:
            snakemake_str += line

    start_rule_lis = start_rule_re.findall(snakemake_str)
    finish_rule_lis = finish_rule_re.findall(snakemake_str)
    error_rule_lis = error_rule_re.findall(snakemake_str)

    job_dic = {}
    for start_rule in start_rule_lis:
        start_date = start_rule[0]
        start_date_parse = parse(start_date)

        rule = start_rule[1]
        input_ass = start_rule[2].split('/')[0]
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
        job_dic[jobid] = (job_dic[jobid] + (error_date_parse, ))
        # print(error_rule)

    return job_dic
    # job_dic
    # jobid : rule input_ass, start_date_parse, finish_date_parse 

    # for job, info in job_dic.items():
    #     running_time = str((info[3] - info[2]))
    #     print(info[0] + ": " + job + info[1] + " " + running_time)

def main():
    dic = log2dic(r'D:\new_ncbi_dataset\tmp_code\sel_Rhodophyta\2022-03-04T193108.332047.snakemake.log')
    for jobid, info in dic.items():
        print(jobid, info)

if __name__ == '__main__':
    main()

