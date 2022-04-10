import snakemake_job_parser
import os

def is_error_log(snakemake_dic):
    if snakemake_dic == "SyntaxError" or snakemake_dic == "SyntaxError" or not isinstance(snakemake_dic, dict):
        return True
    return False

log_top = r'C:\Users\lr201\code\gene_prediction_pipeline\log_test'
log_lis = os.listdir(log_top)

# cat all snakemake logs into a big file
# log = r'C:\Users\lr201\code\gene_prediction_pipeline\log_test\all.log'

snakemake_dic_lis = []
for log in log_lis:
    log_path = os.path.join(log_top, log)
    snakemake_dic_lis.append(snakemake_job_parser.log2dic(log_path))


job_lis = ['braker2', 'interproscan', 'star_remove', 'diamond']
ass_lis = []

ass_job_dic = {}

for snakemake_dic in snakemake_dic_lis:
    if not is_error_log(snakemake_dic):
        for jobid, info in snakemake_dic.items():
            # '3': ('braker2', 'GCA_002887195.1', datetime.datetime(2022, 3, 3, 18, 58, 44))
            if info[1] not in ass_job_dic:
                ass_job_dic[info[1]] = []
                ass_job_dic[info[1]].append(info[0])
            else:
                ass_job_dic[info[1]].append(info[0])


print(ass_job_dic)



