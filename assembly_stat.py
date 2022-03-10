import os
from Bio import SeqIO

top = r'genomes_rec'

def get_contig_N50(seq, quantile):
    seq_dic = SeqIO.to_dict(SeqIO.parse(seq, 'fasta'))
    seq_dic = dict(sorted(seq_dic.items(), key = lambda item : len(item[1].seq), reverse = True))
    total_len = 0

    len_list = []
    for id, record in seq_dic.items():
        total_len += len(record.seq)
        len_list.append(len(record.seq))
    
    target_len = total_len * (1 - quantile * 0.01)
    index = 0
    while target_len > 0:
        target_len -= len_list[index]
        index += 1
    return len_list[index]

def get_contig_num(seq):
    seq_dic = SeqIO.to_dict(SeqIO.parse(seq, 'fasta'))
    contig_num = len(seq_dic)
    return contig_num

def get_genome_size(seq):
    size = 0
    seq_dic = SeqIO.to_dict(SeqIO.parse(seq, 'fasta'))
    for id, record in seq_dic.items():
        size += len(record.seq)
    return size



def main():
    print(get_contig_num(r'D:\new_ncbi_dataset\tmp_code\test\assembly_stat_test.fna'))
    print(get_contig_N50(r'D:\new_ncbi_dataset\tmp_code\test\assembly_stat_test.fna', 50))
    print(get_genome_size(r'D:\new_ncbi_dataset\tmp_code\test\assembly_stat_test.fna'))

if __name__ == '__main__':
    main()