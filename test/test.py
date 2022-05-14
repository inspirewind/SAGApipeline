# import os
# import shutil
# from tqdm import tqdm


# src_top = r'/mnt/d/new_ncbi_dataset/genomes_rec_busco/final_results'
# dst_top = r'/mnt/d/new_ncbi_dataset/genomes_rec_busco/protein/auto'

# ass_lis = os.listdir(src_top)
# ass_lis = [ass for ass in ass_lis if 'GCA' in ass]

# bar_lis = tqdm(ass_lis)
# for ass in bar_lis:
#     busco_src = os.path.join(src_top, ass, 'busco_output_dir')
#     if os.path.exists(busco_src):
#         # print(os.path.join(dst_top, ass))
#         shutil.copytree(busco_src, os.path.join(dst_top, ass))
#     bar_lis.set_description(f'ass: {ass}')

a = 0
print((a := 3))