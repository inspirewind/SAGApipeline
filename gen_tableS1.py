import os
from assembly_stat import get_genome_size

from ncbi_datasets_resolver import resolve_ass_json, print_ass_json

# acc lineages species taxid ass-level ori_annotation size
main_dic = {}
store_top = r'D:\new_ncbi_dataset\genomes_store'
rec_top = r'D:\new_ncbi_dataset\genomes_rec'
ncbi_dir = r'ncbi_dataset\data'

lineage_lis = os.listdir(store_top)
for lineage in lineage_lis:
    ass_json_lis = resolve_ass_json(os.path.join(store_top, lineage, 'ncbi_dataset', 'data', 'assembly_data_report.jsonl'))
    for ass_json in ass_json_lis:
        assAccession = ass_json['assemblyInfo']['assemblyAccession']
        species = ass_json['organismName']
        taxid = ass_json['taxId']
        level = ass_json['assemblyInfo']['assemblyLevel']
        try:
            ori_annotation = ass_json['annotationInfo']['name']  
        except KeyError as e:
            ori_annotation = 'None'
        try:
            non_coding_num = ass_json['annotationInfo']['stats']['geneCounts']['nonCoding']
        except KeyError as e:
            non_coding_num = 0
        try:
            coding_num = ass_json['annotationInfo']['stats']['geneCounts']['proteinCoding']
        except KeyError as e:
            coding_num = 0
        size = get_genome_size(os.path.join(rec_top, lineage, assAccession, 'genome_hf.fna'))
        contig_N50 = ass_json['assemblyStats']['contigN50']
        contig_num = ass_json['assemblyStats']['numberOfComponentSequences']

        if 'GCF' not in assAccession:
            print(assAccession, lineage, species, taxid, level, ori_annotation, non_coding_num, coding_num, size, contig_N50, contig_num, sep = ',')