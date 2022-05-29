import os
import shutil
from tqdm import tqdm

# join_lis_top: ass
ass = None
extract_top = r'F:\final_results'
release_components_item = ['braker2_ep', 'braker2_es', 'interproscan', 'nr_expand_blast', 'non_coding', 'busco']
mode_lis, strategy_lis = ['genome', 'protein'], ['LCA', 'recommend', 'auto']
busco_product = [f'{mode}\{strategy}' for mode in mode_lis for strategy in strategy_lis]

release_components_join = {
    'braker2_ep': [r'braker'], 
    'braker2_es': [r'braker'],
    'interproscan': [r'braker\interproscan.tsv'],
    'nr_expand_blast': [r'braker\matches.tsv'],
    'non_coding': [],
    'busco': busco_product,
    'RefSeq_comp': [],
    # 'genome_hf': [r'genome_hf.fna'],
}

release_components_top = {
    'braker2_ep': r'D:\new_ncbi_dataset\genomes_rec_part',
    'braker2_es': r'D:\new_ncbi_dataset\genomes_rec_es',
    'interproscan': r'D:\new_ncbi_dataset\genomes_rec_part',
    'nr_expand_blast': r'D:\new_ncbi_dataset\genomes_rec_part',
    'non_coding': r'D:\new_ncbi_dataset\genomes_rec_nc',
    'busco': r'E:\genomes_rec_busco\optimize_ass',
    # 'genome_hf': r'D:\new_ncbi_dataset\genomes_rec_part',
}


def init():
    ass_lis = os.listdir(release_components_top['braker2_ep']) # can get 279 ass
    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
    print(f'get {len(ass_lis)} assembly')

    for ass in ass_lis:
        if os.path.exists(os.path.join(extract_top, ass)):
            pass
        else:
            os.makedirs(os.path.join(extract_top, ass))

def extract(item):
    ass_lis = os.listdir(extract_top)
    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
    src_ass_lis = os.listdir(release_components_top[item])

    bar_ass_lis = tqdm(ass_lis)
    for ass in bar_ass_lis:
        file_lis = release_components_join[item]
        
        if len(file_lis) == 0 or 'braker' in item:
            src_path = os.path.join(release_components_top[item], ass)
            dst_path = os.path.join(extract_top, ass, item)
            if os.path.exists(src_path) and not os.path.exists(dst_path):
                shutil.copytree(src_path, dst_path)
        elif 'interproscan' in item or 'nr_expand_blast' in item:
            os.makedirs(os.path.join(extract_top, ass, item), exist_ok=True)
            for file in file_lis:
                src_file = os.path.join(release_components_top[item], ass, file)
                dst_path = os.path.join(extract_top, ass, item)
                dst_file = os.path.join(dst_path, os.path.basename(file))
                if os.path.exists(src_file) and not os.path.exists(dst_file):
                    shutil.copy(src_file, dst_path)
        else:
            os.makedirs(os.path.join(extract_top, ass, item), exist_ok=True)
            for file in file_lis:
                src_path = os.path.join(release_components_top[item], ass, file)
                dst_path = os.path.join(extract_top, ass, item, file)
                if os.path.exists(src_path) and not os.path.exists(dst_path):
                    shutil.copytree(src_path, dst_path)
                

        bar_ass_lis.set_description(f'item: {item}, ass: {ass}')

def remove():
    pass

def inspect():
    ass_lis = os.listdir(extract_top)
    for ass in ass_lis:
        finish_lis = []
        for item in release_components_item:
            if os.path.exists(os.path.join(extract_top, ass, item)):
                file_lis = os.listdir(os.path.join(extract_top, ass, item))
                if len(file_lis) == len(release_components_join(ass)[item]):
                    finish_lis.append({item: 'pass'})
                else:
                    finish_lis.append({item: [file_lis]})
        print(f'{ass}: {finish_lis}')            


def main():
    init()

    for item in release_components_item:
        extract(item)

    # inspect()

if __name__ == '__main__':
    main()




# other_results_item = ['braker2_es', 'braker2_ep', 'busco', 'orf_db', 'genome_hf', 'genome_ori']
# other_results_join = {
#     'braker2_es': [r'braker\braker.gff3', r'braker\augustus.hints.aa', r'braker\augustus.hints.codingseq'],
#     'braker2_ep': [r'braker\braker.gff3', r'braker\augustus.hints.aa', r'braker\augustus.hints.codingseq'],
#     'busco': [],
#     'orf_db': [],

#     'genome_ori': [],
# }
# other_results_top = {}

# def release_components_join(ass):
#     release_components_join_var = {
#         'braker2_ep': [r'braker'], 
#         'interproscan': [r'braker\interproscan.tsv'],
#         'nr_expand_blast': [r'braker\matches.tsv'],
#         'non_coding': [],
#         'busco': busco_product,
#         'RefSeq_comp': [],
#         'genome_hf': [r'genome_hf.fna'],
#         }
#     return release_components_join_var