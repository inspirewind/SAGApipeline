import os
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

# mode_lis = ['genome', 'protein']
# type_lis = ['LCA', 'recommend', 'auto']
# for mode in mode_lis:
#     for type in type_lis:
#         print(mode, type)

# top = r'D:\new_ncbi_dataset\genomes_rec_busco\protein\recommend\Xanthophyceae_2833'
# print(os.listdir(top))

mode_lis = ['genome', 'protein']
strategy_lis = ['LCA', 'recommend', 'auto']
for mode, strategy in zip(mode_lis, strategy_lis):
    print(mode, strategy)