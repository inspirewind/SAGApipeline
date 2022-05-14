import os
import shutil
import time
from tqdm import tqdm

# join_lis_top: ass
ass = None
release_components_item = ['braker2_ep', 'interproscan', 'nr_expand_blast', 'Rfam', 'tRNAscan-se', 'genome_hf']

def release_components_join(ass):
    release_components_join_var = {
        'braker2_ep': [r'braker\braker.gff3', r'braker\augustus.hints.aa', r'braker\augustus.hints.codingseq'], 
        'interproscan': [r'braker\interproscan.tsv'],
        'nr_expand_blast': [r'braker\matches.tsv'],
        'Rfam': [f'{ass}.cmscan', f'{ass}.tblout'],
        'tRNAscan-se': [f'{ass}.out', f'{ass}.stats', f'{ass}.ss'],
        'genome_hf': [r'genome_hf.fna'],
        }
    return release_components_join_var
release_components_top = {
    'braker2_ep': r'D:\new_ncbi_dataset\genomes_rec_part',
    'interproscan': r'D:\new_ncbi_dataset\genomes_rec_part',
    'nr_expand_blast': r'D:\new_ncbi_dataset\genomes_rec_part',
    'Rfam': r'D:\new_ncbi_dataset\genomes_rec_nc',
    'tRNAscan-se': r'D:\new_ncbi_dataset\genomes_rec_nc',
    'genome_hf': r'D:\new_ncbi_dataset\genomes_rec_part',
}

other_results_item = ['braker2_es', 'braker2_ep', 'busco', 'orf_db', 'genome_hf', 'genome_ori']
other_results_join = {
    'braker2_es': [r'braker\braker.gff3', r'braker\augustus.hints.aa', r'braker\augustus.hints.codingseq'],
    'braker2_ep': [r'braker\braker.gff3', r'braker\augustus.hints.aa', r'braker\augustus.hints.codingseq'],
    'busco': [],
    'orf_db': [],

    'genome_ori': [],
}
other_results_top = {}

extract_top = r'D:\new_ncbi_dataset\final_results'

non_coding_top = r'D:\new_ncbi_dataset\genomes_rec_nc'
# print(os.listdir(non_coding_top))

def init():
    ass_lis = os.listdir(release_components_top['braker2_ep'])
    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
    # print(ass_lis)
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
        file_lis = release_components_join(ass)[item]
        os.makedirs(os.path.join(extract_top, ass, item), exist_ok=True)
        if ass in src_ass_lis:
            for file in file_lis:
                src_file = os.path.join(release_components_top[item], ass, file)
                dst_path = os.path.join(extract_top, ass, item)
                dst_file = os.path.join(dst_path, os.path.basename(file))
                if os.path.exists(src_file) and not os.path.exists(dst_file):
                    shutil.copy(src_file, dst_path)
        bar_ass_lis.set_description(f'item: {item}, ass: {ass}')


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

    inspect()

if __name__ == '__main__':
    main()