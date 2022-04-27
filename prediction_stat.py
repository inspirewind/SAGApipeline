import re
from Bio import SeqIO

from snakemake_job_parser import log2dic
import busco_resolver


def get_gene_num(pred_aa):
    seq_dic = SeqIO.to_dict(SeqIO.parse(pred_aa, 'fasta'))
    return len(seq_dic)

def get_interproscan_item_num(ips_tsv):
    line_num = 0
    file = open(ips_tsv, 'r')
    for line in file:
        line_num += 1
    file.close()
    return line_num

def get_running_time(snakemake_dic : dict, ass, rule) -> int:
    # {jobid : (rule, input_ass, start_date_parse, finish_date_parse)}
    for job, info in snakemake_dic.items():
        if ass in info[1] and info[0] == rule:
            return str((info[3] - info[2]).total_seconds())

def get_matches_num():
    pass


def main():
    # snakemake_dic = log2dic(r'D:\new_ncbi_dataset\result\sel_Haptophyta_2830\.snakemake\log\2022-03-03T231159.055539.snakemake.log')
    # get_running_time(snakemake_dic, 'GCA_019693415.1', 'braker2')
    res_lis = busco_resolver(r'D:\new_ncbi_dataset\tmp_code\sel_Rhodophyta\short_summary.specific.chlorophyta_odb10.GCA_001275005.1_augustus.ab_initio.aa.busco.txt')
    print(get_busco_count(res_lis))

if __name__ == '__main__':
    main()