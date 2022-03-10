import os
from ncbi_datasets_resolver import resolve_ass_json
from ncbi_datasets_resolver import get_ass_list_from_json
import shutil

# genomes_store or genomes_rec
store_top = r'/mnt/d/new_ncbi_dataset/genomes_store'
rec_top = r'/mnt/d/new_ncbi_dataset/genomes_rec_part'

# lineage_taxid/ncbi_dataset/assembly_data_report.jsonl
lineage_lis = os.listdir(store_top)

# create lineage-ass map
line_ass_dic = {}
for lineage in lineage_lis:
    ass_json_lis = resolve_ass_json(os.path.join(store_top, lineage, 'ncbi_dataset', 'data', 'assembly_data_report.jsonl'))
    ass_list = get_ass_list_from_json(ass_json_lis)
    line_ass_dic[lineage] = ass_list

def parse_full_lineage(part):
    part = str(part)
    for i in line_ass_dic.keys():
        if part in i:
            return i 

def select_lineage(taxid):
    select_ass_lis = line_ass_dic[parse_full_lineage(taxid)]
    dir_name = 'sel_' + str(parse_full_lineage(taxid))
    print(dir_name + ' ' + str(len(select_ass_lis)))
    print(select_ass_lis)

    # os.makedirs(os.path.join(rec_top, dir_name))
    # for ass in select_ass_lis:
    #     source_path = os.path.join(r'/mnt/d/new_ncbi_dataset/genomes_rec', get_full(taxid), ass)
    #     dis_path = os.path.join(rec_top, dir_name, ass)
    #     shutil.copytree(source_path, dis_path)
    

select_lineage(2825)