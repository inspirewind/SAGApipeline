import os
import shutil
from tqdm import tqdm


lineage_lis = ['Charophyceae_304574', 'Chlorarachniophyceae_29197', 
'Chlorokybophyceae_131213', 'Chlorophyte_3041', 'Chrysophyceae_2825', 
'Cryptophtceae_3027', 'Diatoms_2836', 'Dinophyceae_2864', 'Euglenida_3035', 
'Eustigmatophyceae_5747', 'Glaucocystophyceae_38254', 'Haptophyta_2830', 
'Klebsormidiophyceae_131220', 'Mesostigmatophyceae_96475', 'Phaeophyceae_2870', 
'Rhodophyta_2763', 'Xanthophyceae_2833']

rec_top = r'F:\genomes_rec'
src_top = r'D:\new_ncbi_dataset\genomes_rec_part'
busco_top = r'D:\new_ncbi_dataset\genomes_rec_busco\protein\recommend'

done_num = 0

for lineage in lineage_lis:
    lineage_top = os.path.join(rec_top, lineage)
    ass_lis = os.listdir(lineage_top)
    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
    
    bar_lis = tqdm(ass_lis)

    for ass in bar_lis:
        busco_src = os.path.join(src_top, ass, 'busco_output_dir')
        busco_dst = os.path.join(busco_top, lineage, ass)

        aa_src = os.path.join(src_top, ass, 'braker', 'augustus.hints.aa')
        aa_dst = os.path.join(busco_top, lineage, ass, 'augustus.hints.aa')

        # if os.path.exists(busco_dst):
        #     print('busco output copy done!')
        #     done_num += 1 
        # if os.path.exists(busco_src) and not os.path.exists(busco_dst):
        #     shutil.copytree(busco_src, busco_dst)

        if os.path.exists(aa_src) and not os.path.exists(aa_dst):
            os.makedirs(os.path.dirname(aa_dst))
            shutil.copy(aa_src, aa_dst)
        else:
            print('something wrong!')
            done_num += 1

        bar_lis.set_description(f'lineage: {lineage}, ass: {ass}')

print(done_num)