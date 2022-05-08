import os
import shutil

part_top = r'D:\new_ncbi_dataset\genomes_rec_part'
part_lis = os.listdir(part_top)

chl_path = r'D:\new_ncbi_dataset\genomes_rec_part\done_dia_Chlorophyte_3041'
chl_aa_lis = []
ass_lis = os.listdir(chl_path)
for ass in ass_lis:
    ass_path = os.path.join(chl_path, ass)
    ass_genome_path = os.path.join(ass_path, 'genome_hf.fna')
    ass_aa_path = os.path.join(ass_path, 'braker', 'augustus.hints.aa')
    if os.path.exists(ass_aa_path) and os.path.exists(ass_genome_path):
        chl_aa_lis.append(ass_aa_path)
        print(ass_aa_path)
        busco_top = r'D:\new_ncbi_dataset\genome_rec_busco\protein\Chlorophyte_3041'
        busco_ass_path = os.path.join(busco_top, ass)
        os.makedirs(busco_ass_path)
        shutil.copy(ass_aa_path, busco_ass_path)
        # print()
print(len(chl_aa_lis))