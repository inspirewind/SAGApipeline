import os, shutil
from ncbi_datasets_resolver import get_ass_list_from_json, list_lineage, resolve_ass_json

# store_top = r"D:\new_ncbi_dataset\genomes_store"
# rec_top = r''
# output_file_lis = []

# lineage_list = list_lineage(store_top)
# for lineage in lineage_list:
#     ass_json_lis = resolve_ass_json(os.path.join(lineage, 'assembly_data_report.jsonl'))
#     ass_list = get_ass_list_from_json(ass_json_lis)
#     for ass in ass_list:
#         print(ass)


def detect(top, filename, remain=True):
    result_lis = []
    ass_lis = os.listdir(top)
    for ass in ass_lis:
        if 'GCA' in ass:
            file_path = os.path.join(top, ass, 'braker', filename)
            if os.path.exists(file_path):
                result_lis.append(ass)
    if remain:
        return list(set(ass_lis) - set(result_lis))
    else:
        return result_lis

def transfer(original_top, target_top, filename):
    result_lis = detect(original_top, filename)
    for ass in result_lis:
        ori_file_path = os.path.join(original_top, ass, filename)
        tar_dir_path = os.path.join(target_top, ass)
        if os.path.exists(tar_dir_path) and os.path.exists(tar_dir_path):
            shutil.copy(ori_file_path, tar_dir_path)
        else:
            print(f'{ass} is not exist!')




def main():
    Ch_top = r'E:\done_dia_Chlorophyte_3041'
    print(detect(Ch_top, 'interproscan.tsv'))

if __name__ == '__main__':
    main()


