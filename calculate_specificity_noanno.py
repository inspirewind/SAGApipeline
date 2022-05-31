import os
from Bio import SeqIO
from diamond_tsv_resolver import *
from ncbi_datasets_resolver import ass2lineage

ass_top = r'D:\new_ncbi_dataset\final_results'
ass_lis = os.listdir(ass_top)
for ass in ass_lis:
    matches_path = os.path.join(ass_top, ass, 'nr_expand_blast', 'matches.tsv')
    aa_pred_path = os.path.join(ass_top, ass, 'braker2_ep', 'braker', 'augustus.hints.aa')
    ips_path = os.path.join(ass_top, ass, 'interproscan', 'interproscan.tsv')
    
    all_exist = os.path.exists(matches_path) and os.path.exists(aa_pred_path) and os.path.exists(ips_path)
    
    if all_exist:
        dtr = Diamond_tsv_resolver(matches_path, aa_pred_path, ips_path)
        
        ips, dia = dtr.ips_lis, dtr.blast_lis
        no_ips, no_dia = dtr.no_ips_lis, dtr.no_ali_lis
        all_in, all_out = set(ips) & set(dia), set(no_ips) & set(no_dia)
        ips_nodia, dia_noips = dtr.no_ali_in_ips_lis, dtr.no_ips_in_ali_lis
        
        tp_set = set(ips) & set(dia)
        fn_set = set(no_ips) & set(no_dia)
        tp, fn = len(tp_set), len(fn_set)
        sensitivity = float(tp) / (tp + fn)
        
        print(f'ass: {ass}, total: {len(dtr.query_prs_lis)}, tp: {tp}, fn: {fn}')
        print(f'all in: {len(all_in)}, all out: {len(all_out)}, ips_nodia: {len(ips_nodia)}, dia_noips: {len(dia_noips)}')
        print(f"sensitivity: {sensitivity:.8f}")
 
        

