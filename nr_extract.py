import gzip
from numba import jit
from Bio import SeqIO

matches_lis = []
with open(r'E:\matches_id.txt') as f:
    for line in f:
        matches_lis.append(line.replace('\n', ''))

set_lis = set(matches_lis)
matches_lis = list(set_lis)
print(len(matches_lis) - len(set_lis))

nr_len = 455043919

nr_extract = open(r'E:\nr_extract.fasta', "a+")
nr_extract_des = open(r'E:\nr_extract_des.fasta', "a+")
nr = SeqIO.parse(r'E:\nr', 'fasta')
cnt = 0
nr_idx = 0

for pr in nr:
    if pr.id in set_lis:
        cnt += 1
        nr_extract.write('>' + str(pr.id) + '\n' + str(pr.seq) + '\n')

        # nr_extract.flush()
        # no effect ?

        nr_extract_des.write('>' + str(pr.description) + '\n' + str(pr.seq) + '\n')
        print("nr_idx: " + str(nr_idx) + " cnt: " + str(cnt) + " comp: {:.2f}%".format(nr_idx/nr_len))
    nr_idx += 1

if cnt == len(matches_lis):
    print("all match!")
else:
    print("something wrong QAQ")