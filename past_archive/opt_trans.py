import os
import shutil
from tqdm import tqdm

optimize_top = r'E:\new_ncbi_dataset\result_optimize'
trans_top = r'E:\new_ncbi_dataset\opt_trans'
ass_lis = os.listdir(optimize_top)

mode_lis, strategy_lis = ['genome', 'protein'], ['LCA', 'recommend', 'auto']
product_lis = [f'{mode}\{strategy}' for mode in mode_lis for strategy in strategy_lis]

bar_lis = tqdm(ass_lis)
for ass in bar_lis:
    for product in product_lis:
        src_path = os.path.join(optimize_top, ass, product)
        if os.path.exists(src_path):
            dst_path = os.path.join(trans_top, product, ass)
            shutil.copytree(src_path, dst_path)
            bar_lis.set_description(f'{ass}')

