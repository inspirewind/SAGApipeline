import os
from assembly_stat import get_contig_N50, get_contig_num, get_genome_size
from prediction_stat import get_gene_num, get_interproscan_item_num, get_running_time
from ncbi_datasets_resolver import resolve_ass_json, get_ass_list_from_json
from snakemake_log_resolver import log_path2job


store_top = r'D:\new_ncbi_dataset\genomes_store'
lineage_lis = os.listdir(store_top)
line_ass_dic = {}
for lineage in lineage_lis:
    ass_json_lis = resolve_ass_json(os.path.join(store_top, lineage, 'ncbi_dataset', 'data', 'assembly_data_report.jsonl'))
    ass_list = get_ass_list_from_json(ass_json_lis)
    for ass in ass_list:
        if 'GCF' in ass:
            ass_list.remove(ass)
    line_ass_dic[lineage] = ass_list

def get_real_anno_num():
    ass_num = 0
    for lineage, ass_list in line_ass_dic.items():
        ass_num += len(ass_list)
    return ass_num
# print(line_ass_dic)


pred_aa_join = r'braker\augustus.hints.aa'
braker_anno_join = r'braker\braker.gtf'
interproscan_join = r'braker\interproscan.tsv'
genome_join = r'genome_hf.fna' # stat genom_size
matches_join = r'braker\matches.tsv'
busco_join = r''


result_top = r'D:\new_ncbi_dataset\genomes_rec_part'
part_lis = os.listdir(result_top)
for part in part_lis:
    if 'done_ips_dia' in part:
        lineage_path = os.path.join(result_top, part)
        lineage_smk_log_path = os.path.join(lineage_path, '.snakemake', 'log')

        ass_job_dic = log_path2job(lineage_smk_log_path)
        # ass_job_dic = {ass1: [('braker2', start_time, finish_time), 'interproscan', 'star_remove', 'diamond'], ass2: ...}
        for ass, jobs in ass_job_dic.items():
            print(ass, jobs)
        print(len(ass_job_dic))



        # for ass in ass_job_dic:
        #     pred_aa_path = os.path.join(lineage_path, pred_aa_join)
        #     braker_anno_path = os.path.join(lineage_path, braker_anno_join)
        #     interproscan_path = os.path.join(lineage_path, interproscan_join)
        #     genome_path = os.path.join(lineage_path, genome_join)
        #     matches_path = os.path.join(lineage_path, matches_join)

            
        #     # TODO: log2dic is only used in snakemake_log_resolver.py
        #     # using the interface in snakemake_job_parser.py to get jobdic directly
        #     job_dic = log2dic(snakemake_path)

        #     # busco_path = os.path.join('')
        #     # busco_count = get_busco_count()
            
        #     contig_N50 = get_contig_N50(genome_path, 50)
        #     contig_num = get_contig_num(genome_path)
        #     genome_size = get_genome_size(genome_path)
        #     gene_num = get_gene_num(pred_aa_path)
        #     ips_item_num = get_interproscan_item_num(interproscan_path)
        #     running_time = get_running_time(job_dic, ass, 'braker2')

        #     print(ass, contig_N50, contig_num, genome_size, gene_num, ips_item_num, running_time)