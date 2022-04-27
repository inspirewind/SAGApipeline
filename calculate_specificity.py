import os
from diamond_tsv_resolver import *
# TP: pred: T, real: T
# FP: pred: T, real: F
# tp + fp = total_pred

res_top = r'C:\Users\lr201\code\gene_prediction_pipeline\test\GCA_000091205.1'
dtr = Diamond_tsv_resolver(os.path.join(res_top, 'matches.tsv'), os.path.join(res_top, 'augustus.hints.aa'), os.path.join(res_top, 'interproscan.tsv'))
print(f"full_match_rate: {dtr.get_full_match_rate():.8f}")
print(f"no_ali_rate: {dtr.get_no_ali_rate():.8f}")
print(f"mean evalue: {dtr.mean_evalue():.8f}")
print(f"no_ali_lis: {len(dtr.get_no_ali_lis())}")
print(f"no ali but in ips: {dtr.get_no_ali_in_ips_lis()}")      
print()

total_pred = len(dtr.pred_prs_lis)
fp = len(dtr.no_ali_lis) - len(dtr.no_ali_in_ips_lis)
tp = total_pred - fp
sp = tp / (tp + fp)

fp_strict = len(dtr.no_ali_lis)
tp_strict = total_pred - fp_strict
sp_strict = tp_strict / (tp_strict + fp_strict)


print(f'total_pred: {total_pred}')
print(f'fp: {fp}')
print(f'tp: {tp}')
print(f'sp: {sp:.8f}')
print(f'sp_strict: {sp_strict}')
print(f'diff: {sp - sp_strict:.8f}')