import os
from prediction_stat import get_gene_num


# ep_top = r'D:\new_ncbi_dataset\genomes_rec_part'
# es_top = r'D:\new_ncbi_dataset\genomes_rec_es'
ep_top = r'/mnt/d/new_ncbi_dataset/genomes_rec_part'
es_top = r'/mnt/d/new_ncbi_dataset/genomes_rec_es'
# print(os.listdir(es_top))

print("ass, num, mode")

ass_lis = os.listdir(ep_top)
ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
for ass in ass_lis:
    ep_ass_path = os.path.join(ep_top, ass)
    es_ass_path = os.path.join(es_top, ass)

    ep_aa_path = os.path.join(ep_ass_path, 'braker', 'augustus.hints.aa')
    es_aa_path = os.path.join(es_ass_path, 'braker', 'augustus.ab_initio.aa')

    if os.path.exists(ep_aa_path) and os.path.exists(es_aa_path):
        ep_gene_num = get_gene_num(ep_aa_path)
        es_gene_num = get_gene_num(es_aa_path)
        print(f'{ass}, {es_gene_num}, es')
        print(f'{ass}, {ep_gene_num}, ep')
        # print(f'{ass}, {ep_gene_num}, {es_gene_num}')