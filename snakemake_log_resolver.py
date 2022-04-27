import snakemake_job_parser
import os

job_lis = ['braker2', 'interproscan', 'star_remove', 'diamond']

def is_error_log(snakemake_dic): 
    if not isinstance(snakemake_dic, dict):
        # error log will return a string
        return True
    return False

# def get_braker2_finished_lis(snakemake_log):
#     fin_lis = []
#     job_dic = log2dic(snakemake_log)
#     info_lis =  job_dic.values()
#     for info in info_lis:
#         fin_lis.append(info[1].strip())
#     return fin_lis

def log_path2job(log_top):
    # log_top: .snakemake/log/

    log_lis = os.listdir(log_top)
    snakemake_dic_lis = []
    for log in log_lis:
        log_path = os.path.join(log_top, log)
        snakemake_dic_lis.append(snakemake_job_parser.log2dic(log_path))

    ass_job_dic = {}

    for snakemake_dic in snakemake_dic_lis:
        if not is_error_log(snakemake_dic):
            for jobid, info in snakemake_dic.items():
                # print(jobid, info)
                # '3': ('braker2', ass, start_datetime, finish_datetime)
                if info[1] not in ass_job_dic:
                    ass_job_dic[info[1]] = []
                    if info[0] == 'braker2':
                        ass_job_dic[info[1]].append(('braker2', info[2], info[3]))
                    else:
                        ass_job_dic[info[1]].append(info[0])
                else:
                    ass_job_dic[info[1]].append(info[0])
    return ass_job_dic


def main():
    log_top = r'D:\new_ncbi_dataset\genomes_rec_part\done_ips_dia_Diatoms_2836\.snakemake\log'
    ass_job_dic = log_path2job(log_top)
    for ass, jobs in ass_job_dic.items():
        print(ass, jobs)
    print(len(ass_job_dic))

if __name__ == '__main__':
    main()

