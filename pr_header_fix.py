import os
from Bio import SeqIO

prot_seq_path = r'/mnt/d/new_ncbi_dataset/pr_mix_total_uaf.fasta'
fix_pr_tmp_path = prot_seq_path.replace('pr_mix_total_uaf.fasta', "pr_mix_total_uaf_tmp.fasta")
fix_pr_path = prot_seq_path.replace('pr_mix_total_uaf.fasta', "pr_mix_total_uaf_hf.fasta")

prot_seq = SeqIO.parse(prot_seq_path, "fasta")
fixed_seq = open(fix_pr_tmp_path, 'a+')
for pr in prot_seq:
    # " " -> "_", "|" -> "__"
    fixed_seq.write('>' + str(pr.id).replace(" ", "_").replace("|", "__") + '\n' + str(pr.seq) + '\n')


refine = SeqIO.parse(fix_pr_tmp_path, 'fasta')
prot_num = SeqIO.write(refine, fix_pr_path, 'fasta')
print(prot_num)