import os
from diamond_tsv_resolver import *

top = r'/mnt/d/new_ncbi_dataset/final_results'
ass_lis = os.listdir(top)
print("ass, full_match_rate, mean_evalue")
for ass in ass_lis:
    match_path = os.path.join(top, ass, 'nr_expand_blast', 'matches.tsv')
    aa_pred_path = os.path.join(top, ass, 'braker2_ep', 'braker', 'augustus.hints.aa')
    
    all_exist = os.path.exists(match_path) and os.path.exists(aa_pred_path)
    if all_exist:
        dtr = Diamond_tsv_resolver(match_path, aa_pred_path)
        print(f'{ass}, {dtr.get_full_match_rate()}, {dtr.get_mean_evalue()}')
        