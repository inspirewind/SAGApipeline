import decimal
import statistics
import os
import numpy as np

class Diamond_tsv_resolver:
    def __init__(self, tsv, query_prs, ips=None) -> None:
        self.e_value_lis = [] # e_value_lis, len = diamond alignment items number, one gene can have multiple alignments
        self.dec_evalue_lis = []
        self.query_prs_lis = [] # seqs in augustus.hints.aa
        self.blast_lis = [] # genes that have blast alignment
        self.ips_lis = [] # genes that have interproscan annotation
        
        self.no_ali_lis = [] # all no ali gene, including no ali but in ips and no ips
        self.no_ali_in_ips_lis = [] # no ali but in ips (new gene maybe)
        self.no_ips_lis = []
        self.no_ips_in_ali_lis = []
        
        # use for ORF classifier
        self.coding_lis = []
        self.no_coding_lis = []
        
        (self.tsv, self.query_prs, self.ips) = (tsv, query_prs, ips)

        # load evalue
        # set self.e_value_lis
        with open(self.tsv) as f:
            evalue = np.loadtxt(f, dtype = 'float', delimiter = '\t', usecols = 10)
            self.e_value_lis = list(evalue)
        # using decimal always
        # set self.dec_evalue_lis
        for evalue in self.e_value_lis:
            if evalue is not None:
                self.dec_evalue_lis.append(decimal.Decimal(evalue))

        # self.quert_prs: augustus.hints.aa
        # self.query_prs_lis: seqs in augustus.hints.aa, they are the query seqs in diamond,
        # but are not equal to set(self.blast_lis) because a little seqs have no blast alignment
        with open(self.query_prs) as f:
            for line in f:
                if line.startswith('>'):
                    self.query_prs_lis.append(line.replace('>', '').replace('\n', ''))

        # load augustus' gene id in matches result
        # set self.blast_lis
        with open(self.tsv) as f:
            genes = np.loadtxt(f, dtype = 'str', delimiter = '\t', usecols = 0)
            # prediction genes that have alignments, had removed the duplicates that one gene have multiple alignments
            self.blast_lis = set(list(genes))
       

        # load NR_expand database id
        with open(self.tsv) as f:
            database_seq = np.loadtxt(f, dtype = 'str', delimiter = '\t', usecols = 1)
            self.coding_lis = set(list(database_seq))

        # self.ips_lis: genes that have interproscan annotation
        if self.ips is not None:
            with open(self.ips) as f:
                ips_ali = np.loadtxt(f, dtype = 'str', delimiter = '\t', usecols = 0)
                self.ips_lis = list(ips_ali)

        self.no_ali_lis = list(set(self.query_prs_lis) - set(self.blast_lis))
        self.no_ips_lis = list(set(self.query_prs_lis) - set(self.ips_lis))
        self.no_ips_in_ali_lis = list(set(self.no_ips_lis) & set(self.blast_lis))
        self.no_ali_in_ips_lis = list(set(self.no_ali_lis) & set(self.ips_lis))
        

    def get_zero_num(self):
        num = 0
        # failed using str.count()
        # return str(evalue_lis).count("0.0")
        for i in self.dec_evalue_lis:
            if decimal.Decimal(i).is_zero():
                num += 1
        return num

    def get_full_match_rate(self):
        full_match_rate = float(self.get_zero_num()) / float(len(self.dec_evalue_lis))
        return float(full_match_rate) 
    
    def get_mean_evalue(self):
        dec_am = statistics.mean(self.dec_evalue_lis)
        return float(dec_am)

    def get_no_ali_rate(self):
        pr_num = len(self.query_prs_lis)
        no_ali_rate = 1.0 - (float(len(self.blast_lis)) / float(pr_num))
        return no_ali_rate
    
 


        
def main():
    res_top = r'C:\Users\lr201\code\gene_prediction_pipeline\test\GCA_000091205.1'
    dtr = Diamond_tsv_resolver(os.path.join(res_top, 'matches.tsv'), os.path.join(res_top, 'augustus.hints.aa'), os.path.join(res_top, 'interproscan.tsv'))
    # print(f"full_match_rate: {dtr.get_full_match_rate():.8f}")
    # print(f"no_ali_rate: {dtr.get_no_ali_rate():.8f}")
    # print(f"mean evalue: {dtr.mean_evalue():.8f}")
    # print(f"no_ali_lis: {len(dtr.get_no_ali_lis())}")
    # print(f"no ali but in ips: {len(dtr.get_no_ali_in_ips_lis())}")
    # print(f"no ips: {len(dtr.get_no_ips_lis())}")
    # print(f"no ips but in ali: {len(dtr.get_no_ips_in_ali_lis())}")
    
    # no RefSeq cal
    ips, dia = dtr.ips_lis, dtr.blast_lis
    no_ips, no_dia = dtr.no_ips_lis, dtr.no_ali_lis
    
    all_in, all_out = set(ips) & set(dia), set(no_ips) & set(no_dia)
    ips_nodia, dia_noips = dtr.no_ali_in_ips_lis, dtr.no_ips_in_ali_lis
    
    tp_set = set(ips) & set(dia)
    fn_set = set(no_ips) & set(no_dia)
    
    print(f'total: {len(dtr.query_prs_lis)}')
    print(f'all in: {len(all_in)}, all out: {len(all_out)}')
    print(f'ips_nodia: {len(ips_nodia)}, dia_noips: {len(dia_noips)}')
    
    tp, fn = len(tp_set), len(fn_set)
    print(f"tp: {tp}, fn: {fn}")
    
    sensitivity = float(tp) / (tp + fn)
    # precision = float(tp) / (tp + fp)
    # f1_score = 2 * (sensitivity * precision) / (sensitivity + precision)
    print(f"sensitivity: {sensitivity:.8f}")


if __name__ == '__main__':
    main()


