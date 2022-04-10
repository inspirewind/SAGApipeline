import decimal
import statistics
import csv
import os
import numpy as np


class Diamond_tsv_resolver:
    def __init__(self, tsv, pred_prs, ips) -> None:
        self.e_value_lis = []
        self.dec_evalue_lis = []
        self.blast_lis = []
        self.ips_lis = []
        self.no_ali_lis = [] 
        self.no_ali_in_ips_lis = [] # no ali but in ips (new gene maybe)
        self.pred_prs_lis = []
        self.tsv, self.pred_prs, self.ips = tsv, pred_prs, ips

        with open(self.tsv) as f:
            evalue = np.loadtxt(f, dtype = 'float', delimiter = '\t', usecols = 10)
            self.e_value_lis = list(evalue)
        with open(self.tsv) as f:
            genes = np.loadtxt(f, dtype = 'str', delimiter = '\t', usecols = 0)
            self.blast_lis = set(list(genes))

        # using decimal always
        for evalue in self.e_value_lis:
            if evalue is not None:
                self.dec_evalue_lis.append(decimal.Decimal(evalue))

        with open(self.pred_prs) as f:
            for line in f:
                if line.startswith('>'):
                    self.pred_prs_lis.append(line.replace('>', '').replace('\n', ''))

        with open(self.ips) as f:
            ips_ali = np.loadtxt(f, dtype = 'str', delimiter = '\t', usecols = 0)
            self.ips_lis = list(ips_ali)

    def get_zero_num(self):
        num = 0
        # failed using str.count()
        # return str(evalue_lis).count("0.0")
        for i in self.dec_evalue_lis:
            if decimal.Decimal(i).is_zero():
                num += 1
        return num

    def get_full_match_rate(self):
        full_match_rate = float(self.get_zero_num()) / float(len(self.dec_evalue_lis)) * 100
        return full_match_rate 
    
    def mean_evalue(self):
        dec_am = statistics.mean(self.dec_evalue_lis)
        return dec_am
    
    def get_no_ali_rate(self):
        pr_num = 0
        with open(self.pred_prs) as f:
            for line in f:
                if '>' in line:
                    pr_num += 1
        
        no_ali_rate = 100.0 - float(len(self.blast_lis)) / float(pr_num) * 100
        return no_ali_rate
    
    def get_no_ali_lis(self):
        pred_prs_set = set(self.pred_prs_lis)
        for pr in pred_prs_set:
            if pr not in set(self.blast_lis):
                self.no_ali_lis.append(pr)
        return(self.no_ali_lis)
    
    def get_no_ali_in_ips_lis(self):
        for no_ali_pr in self.no_ali_lis:
            if no_ali_pr in self.ips_lis:
                self.no_ali_in_ips_lis.append(no_ali_pr)
        return self.no_ali_in_ips_lis

        

res_top = r'C:\Users\lr201\code\gene_prediction_pipeline\test\GCA_000091205.1'
dtr = Diamond_tsv_resolver(os.path.join(res_top, 'matches.tsv'), os.path.join(res_top, 'augustus.hints.aa'), os.path.join(res_top, 'interproscan.tsv'))
print(f"full_match_rate: {dtr.get_full_match_rate():.8f}")
print(f"no_ali_rate: {dtr.get_no_ali_rate():.8f}")
print(f"mean evalue: {dtr.mean_evalue():.8f}")
print(f"no_ali_lis: {len(dtr.get_no_ali_lis())}")
print(f"no ali but in ips: {dtr.get_no_ali_in_ips_lis()}")      


