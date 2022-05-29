import json
import os
from Bio import SeqIO

top = r'/mnt/d/new_ncbi_dataset/genomes_store'
rec = r'/mnt/d/new_ncbi_dataset/genomes_rec'
# top = r'D:\new_ncbi_dataset\genomes'

def print_ass_json(ass_json : dict):
    # recursively print an assembly json information
    for k, v in ass_json.items():
        if isinstance(v, dict):
            print_ass_json(v)
        else:
            print(str(k) + ': ' + str(v))

def resolve_ass_json(file_path):
    json_file = open(file_path)
    ass_json_lis = []
    for line in json_file.readlines():
        dic = json.loads(line)
        ass_json_lis.append(dic)
    return ass_json_lis

def get_ass_list_from_json(ass_json_lis):
    # accepts a parsed json list of multiple assemblies
    ass_acc_lis = []
    for ass in ass_json_lis:
        ass_acc_lis.append(ass['assemblyInfo']['assemblyAccession'])
    return ass_acc_lis

def ass2lineage(ass) -> str:
    ass_line_dic = {}
    # store_top = r'D:\new_ncbi_dataset\genomes_store'
    store_top = r'/mnt/d/new_ncbi_dataset/genomes_store'
    lineage_lis = os.listdir(store_top)
    for lineage in lineage_lis:
        ass_top_path = os.path.join(store_top, lineage, 'ncbi_dataset', 'data')
        ass_lis = os.listdir(ass_top_path)
        ass_line_dic[lineage] = ass_lis
    for lineage in ass_line_dic.keys():
        if ass in ass_line_dic[lineage]:
            return lineage


def list_fna_file(top):
    assembly = os.listdir(top)
    fna = [file for file in assembly if '.fna' in file]
    return fna

def list_lineage(top):
    # top: genomes
    #   -(taxon1_taxid1)
    #   -(taxon2_taxid2)
    species = os.listdir(top)
    species_path = []
    for sp in species:
        sp = os.path.join(top, sp, 'ncbi_dataset', 'data')
        species_path.append(sp)
    return species_path

def is_chr(fna):
    for i in fna :
        if ('chr' in i) and ('Pl' not in i):
            return True
    return False

def get_chr_len_list(ass_path):
    chr_len_list = []
    files = list_fna_file(ass_path)
    for file in files:
        # remove 'chrPltd.unlocalized.scaf.fna'
        if ('chr' in file) and ('Pl' not in file):
            if 'unlocal' in file:
                un_chr = SeqIO.to_dict(SeqIO.parse(os.path.join(ass_path, file), "fasta"))
                chr_len = 0
                for id, record in un_chr.items():
                    chr_len += len(record.seq)
            else:
                chr = SeqIO.read(os.path.join(ass_path, file), "fasta")
                chr_len = len(chr.seq)
            chr_len_list.append(chr_len)
    return chr_len_list

def select_unplace_with_chr(ass_path):
    # not use because min_contig

    seq = os.path.join(ass_path, 'unplaced.scaf.fna')
    unpl_seq = SeqIO.to_dict((SeqIO.parse(seq, "fasta")))
    unpl_seq = dict(sorted(unpl_seq.items(), key = lambda item : len(item[1].seq), reverse = True))
   
    chr_len_list = get_chr_len_list(ass_path)
    len_list = []
    len_dict = {}
    for id, record in unpl_seq.items():
        if len(record.seq) > 20000:
            len_list.append(len(record.seq))
            len_dict[id] = record        

def cat_fna(fna : list):
    # remove non-genome part
    if 'cds_from_genomic.fna' in fna:
        fna.remove('cds_from_genomic.fna')
    if 'rna.fna' in fna:
        fna.remove('rna.fna')
    
    # cat chrs
    cat_fna_lis = str()
    for i in fna:
        cat_fna_lis += (i + ', ')
        
    if cat_fna_lis != '' and len(cat_fna_lis) > 1:
        cat_fna_lis = cat_fna_lis.strip(', ').replace(',', ' ')

        os.system("cat %s > genome.fna" % (cat_fna_lis))

def main():
    ass_cnt = 0
    lineage_list = list_lineage(top)
    for lineage in lineage_list:
        ass_json_lis = resolve_ass_json(os.path.join(lineage, 'assembly_data_report.jsonl'))
        ass_list = get_ass_list_from_json(ass_json_lis)
        for ass in ass_list:
            ass_path = os.path.join(lineage, ass)
            fna_list = list_fna_file(ass_path)
            
            os.chdir(ass_path)
            print("ass_path: " + str(ass_path))

            cat_fna(fna_list)
            print("cated!")


            os.chdir(lineage.replace("genomes_store", "genomes_rec").replace("ncbi_dataset/data", ''))
            os.system("mkdir %s" % ass)
            os.chdir(ass)
            os.system("pwd")

            os.system("mv %s/genome.fna ." % ass_path)

            ass_cnt += 1
            print("ass_cnt" + str(ass_cnt) + '\t' + " comp: " + str(ass_cnt/300*100) + "%")
            print()

if __name__ == '__main__':
    main()
