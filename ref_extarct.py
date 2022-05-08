import os
from shutil import copy

anno_top = r'D:\new_ncbi_dataset\genomes_rec_part'
ref_top = r'D:\new_ncbi_dataset\genomes_ref_comp'

ref_lis = os.listdir(ref_top)
anno_lis = os.listdir(anno_top)

map_lis = []

for ref in ref_lis:
    ref_path = os.path.join(ref_top, ref)
    for part in anno_lis:
        if 'done' in part:
            anno_path = os.path.join(anno_top, part)
            ass_lis = os.listdir(anno_path)
            for ass in ass_lis:
                ass_aa_path = os.path.join(anno_path, ass, 'genome_hf.fna')
                if ass.replace('GCA_', '').split('.')[0] == ref.replace('GCF_', '').split('.')[0] and os.path.exists(ass_aa_path):
                    map_lis.append((ref, part, ass))
                    print(ref_path)
                    print(ass_aa_path)
                    copy(ass_aa_path, ref_path)
                    print()


# print(map_lis)
print(len(map_lis))




