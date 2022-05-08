import os
from assembly_stat import get_contig_N50, get_contig_num, get_genome_size
from prediction_stat import get_gene_num, get_interproscan_item_num, get_running_time
from ncbi_datasets_resolver import resolve_ass_json, get_ass_list_from_json, ass2lineage
from ass_jobs_stat import jobs_stat


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
braker_log_join = r'braker\braker.log'
interproscan_join = r'braker\interproscan.tsv'
genome_join = r'genome_hf.fna' # stat genome_size
matches_join = r'braker\matches.tsv'
busco_join = r''


result_top = r'D:\new_ncbi_dataset\genomes_rec_part'
jobs_stat_dic = jobs_stat(result_top)

for part, stat in jobs_stat_dic.items():
    part_path = os.path.join(result_top, part)

    # ass_lis = os.listdir(os.path.join(result_top, part))
    # ass_lis = [ass for ass in ass_lis if 'GCA' in ass]

    ass_lis = stat['well_done_lis']
    for ass in ass_lis:
        ass_path = os.path.join(part_path, ass)
        pred_aa_path = os.path.join(ass_path, pred_aa_join)
        braker_anno_path = os.path.join(ass_path, braker_anno_join)
        braker_log_path = os.path.join(ass_path, braker_log_join)
        interproscan_path = os.path.join(ass_path, interproscan_join)
        genome_path = os.path.join(ass_path, genome_join)
        matches_path = os.path.join(ass_path, matches_join)

        lineage = ass2lineage(ass).split('_')[0]
        contig_N50 = get_contig_N50(genome_path, 50)
        contig_num = get_contig_num(genome_path)
        genome_size = get_genome_size(genome_path)
        gene_num = get_gene_num(pred_aa_path)
        ips_item_num = get_interproscan_item_num(interproscan_path)
        running_time = get_running_time(braker_log_path)

        print(ass, lineage, contig_N50, contig_num, genome_size, gene_num, ips_item_num, running_time)