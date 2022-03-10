from Bio import SeqIO

def get_N50(seq, quantile):
    seq_dic = SeqIO.to_dict(SeqIO.parse(seq, 'fasta'))
    seq_dic = dict(sorted(seq_dic.items(), key = lambda item : len(item[1].seq), reverse = True))
    total_len = 0

    len_list = []
    for id, record in seq_dic.items():
        total_len += len(record.seq)
        len_list.append(len(record.seq))
    
    target_len = total_len * (quantile * 0.01)
    index = 0
    while target_len > 0:
        target_len -= len_list[index]
        index += 1
    return index


print(get_N50(r'N50_test_seq.fasta', 90))