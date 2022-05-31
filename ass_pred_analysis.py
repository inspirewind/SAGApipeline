import os
from assembly_stat import get_contig_N50, get_contig_num, get_genome_size
from prediction_stat import get_gene_num, get_interproscan_item_num, get_running_time
from ncbi_datasets_resolver import ass2lineage


# pred_aa_join = r'braker2_ep\braker\augustus.hints.aa'
# interproscan_join = r'interproscan\interproscan.tsv'
# genome_join = r'braker2_ep\genome_hf.fna' # stat genome_size
# matches_join = r'nr_expand_blast\matches.tsv'

pred_aa_join = r'braker2_ep/braker/augustus.hints.aa'
interproscan_join = r'interproscan/interproscan.tsv'
genome_join = r'braker2_ep/genome_hf.fna' # stat genome_size
matches_join = r'nr_expand_blast/matches.tsv'

ori_part_top = r'/mnt/d/new_ncbi_dataset/genomes_rec_part'
result_top = r'/mnt/d/new_ncbi_dataset/final_results'
ass_lis = os.listdir(result_top)

print('ass, lineage, contig_N50, contig_num, genome_size, gene_num, ips_item_num, running_time')
for ass in ass_lis:
    ass_path = os.path.join(result_top, ass)
    pred_aa_path = os.path.join(ass_path, pred_aa_join)
    interproscan_path = os.path.join(ass_path, interproscan_join)
    genome_path = os.path.join(ass_path, genome_join)
    matches_path = os.path.join(ass_path, matches_join)
    braker_log_path = os.path.join(ori_part_top, ass, 'braker', 'braker.log')
    
    all_exist = os.path.exists(pred_aa_path) and \
                os.path.exists(interproscan_path) and \
                os.path.exists(genome_path) and \
                os.path.exists(matches_path) and \
                os.path.exists(braker_log_path)
    if all_exist:
        lineage = ass2lineage(ass).split('_')[0]
        contig_N50 = get_contig_N50(genome_path, 50)
        contig_num = get_contig_num(genome_path)
        genome_size = get_genome_size(genome_path)
        gene_num = get_gene_num(pred_aa_path)
        ips_item_num = get_interproscan_item_num(interproscan_path)
        running_time = get_running_time(braker_log_path)

        print(f'{ass}, {lineage}, {contig_N50}, {contig_num}, {genome_size}, {gene_num}, {ips_item_num}, {running_time}')
    else:
        # print(ass)
        pass