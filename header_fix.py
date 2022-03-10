import os
from Bio import SeqIO


def fix(seq):
    seq_parse = SeqIO.parse(seq, 'fasta')
    # get seq abs path
    seq_abs_path = os.path.abspath(seq)
    tmp_path = seq.replace('genome.fna', 'header_fix_tmp.fna')
    fixed_seq = open(tmp_path, 'a+') 
    for contig in seq_parse:
        fixed_seq.write('>' + str(contig.id) + '\n' + str(contig.seq) + '\n')
    
    final_path = seq.replace("genome.fna", 'genome_hf.fna')
    refine = SeqIO.parse(tmp_path, 'fasta')
    contig_num = SeqIO.write(refine, final_path, "fasta")
    
    return contig_num


def main():
    ass_cnt = 0
    top = r'/mnt/d/new_ncbi_dataset/genomes_rec'
    lineages = os.listdir(top)
    for lineage in lineages:
        ass_lis = os.listdir(os.path.join(top, lineage))
        for ass in ass_lis:
            contig_num = fix(os.path.join(top, lineage, ass, 'genome.fna'))
            print("ass_cnt: " + str(ass_cnt) + " contig_num: " + str(contig_num))
            ass_cnt += 1


if __name__ == '__main__':
    main()
