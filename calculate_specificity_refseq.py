from cmath import sqrt
import os
from Bio import SeqIO
from diamond_tsv_resolver import *
from ncbi_datasets_resolver import ass2lineage

# TP: pred: T, real: T
# FP: pred: T, real: F
# tp + fp = total_pred

ref_top = r'D:\new_ncbi_dataset\genomes_ref_comp'
ass_lis = os.listdir(ref_top)

print('ass\t \
        lineage\t \
        total_orf_num\t \
        total_pred\t \
        pred_blast_num\t \
        pred_database_coding\t \
        total_ref\t \
        ref_blast_num\t \
        ref_database_coding\t \
        tp\ttn\tfn\tfp\t \
        sensitivity\tspecificity\tprecision\taccuracy\t \
        f1\tcc\tac')

for ass in ass_lis:
    if 'GCF' in ass:
        lineage = ass2lineage(ass)
        orf_path = os.path.join(ref_top, ass, f'{ass}_ORFfinder.out')
        total_orf_num = len(list(SeqIO.parse(orf_path, 'fasta')))
        pred_dtr = Diamond_tsv_resolver(os.path.join(ref_top, ass, 'ORF_pred_matches.tsv'), os.path.join(ref_top, ass, 'augustus.hints.aa'))
        ref_dtr = Diamond_tsv_resolver(os.path.join(ref_top, ass, 'ORF_ref_matches.tsv'), os.path.join(ref_top, ass, 'protein.faa'))

        
        total_pred = len(pred_dtr.query_prs_lis)
        pred_blast_num = len(pred_dtr.blast_lis)
        pred_database_coding = len(pred_dtr.coding_lis)

        total_ref = len(ref_dtr.query_prs_lis)
        ref_blast_num = len(ref_dtr.blast_lis)
        ref_database_coding = len(ref_dtr.coding_lis)

        orf_list = [seq.id for seq in list(SeqIO.parse(orf_path, 'fasta'))]
        orf_set = set(orf_list)
        ref_coding_set = set(ref_dtr.coding_lis)
        ref_no_coding_set = orf_set - ref_coding_set

        pred_coding_set = set(pred_dtr.coding_lis)
        pred_no_coding_set = orf_set - pred_coding_set

        tp_set = pred_coding_set & ref_coding_set
        tn_set = pred_no_coding_set & ref_no_coding_set
        fn_set = pred_no_coding_set & ref_coding_set
        fp_set = pred_coding_set & ref_no_coding_set
        (tp, tn, fn, fp) = (len(tp_set), len(tn_set), len(fn_set), len(fp_set))

        # sensitivity = tp / (tp + fn)
        # recall, hit rate, TPR: ture positive rate
        sn = tp / (tp + fn)

        # specificity = tn / (tn + fp)
        # selectivity, TNR: true negative rate
        sp = tn / (tn + fp)

        # precision = tp / (tp + fp)
        # PPV: positive predictive value
        pp = tp / (tp + fp)

        # accuracy = (tp + tn) / (tp + tn + fp + fn)
        ac = (tp + tn) / (tp + tn + fp + fn)

        # F1 score: the harmonic mean of sensitivity and precision
        f1 = 2 * sn * pp / (sn + pp)


        # correlation coeffcient
        # cc = ((tp * tn) - (fn * fp)) / sqrt((tp + fn) * (tn + fp) * (tp + fp) * (tn + fn))
        # acp = 0.25 * ( (tp / (tp + fn)) + (tp / (tp + fp)) + (tn / (tn + fp)) + (tn / (tn + fn)) )
        # # approximate correlation 
        # ac = (acp - 0.5) * 2

        # print(f'{ass}\t{lineage}')
        # print(f'total_orf_num: {total_orf_num}')
        # print(f'total_pred: {total_pred}')
        # print(f'pred_blast_num: {pred_blast_num}')
        # print(f'pred_database_coding: {pred_database_coding}')

        # print(f'total_ref: {total_ref}')
        # print(f'ref_blast_num: {ref_blast_num}')
        # print(f'ref_database_coding: {ref_database_coding}')
        # print(f'tp: {len(tp_set)}, tn: {len(tn_set)}, fn: {len(fn_set)}, fp: {len(fp_set)}')
        # print(f'sensitivity: {sn}, specificity: {sp}')
        # print(f'F1 score: {f1}')
        # print(f'cc: {cc}, ac: {ac}')

        # print('-'*50)

        # print for R plot
        
        print(f'{ass}\t{lineage}\t{total_orf_num}\t{total_pred}\t{pred_blast_num}\t{pred_database_coding}\t{total_ref}\t{ref_blast_num}\t{ref_database_coding}\t{tp}\t{tn}\t{fn}\t{fp}\t{sn}\t{sp}\t{pp}\t{ac}\t{f1}')

