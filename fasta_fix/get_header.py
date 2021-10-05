from typing import Counter
import time
import os
import header_fixer

#double Name, Common_Name, Organism_Qualifier, Tax_id, Assembly_Name, Assembly_acc
report_all = r'C:\Users\lr201\code\gene_prediction_pipeline\data_summary.tsv'
genomes_top = r'D:\plantdatabase\plants_genome_new\all'
bams_top = r'D:\plantdatabase\BAMs'

def get_bams(top : str) -> list:
    bams_path = os.listdir(top)
    bams_path_fix = []
    for bam in bams_path:
        bams_path_fix.append(bam.replace('_', ' '))
    return bams_path_fix

def get_genomes(top : str) -> list:
    genomes_path = os.listdir(top)
    return genomes_path

def build_index(all : str) -> dict:
    index = {}
    with open(all) as f:
        for line in f:
            double_name = line.split('\t')[0]
            acc = line.split('\t')[5]
            # print(acc + ": " + double_name)
            index[double_name] = acc
    return index

def indexing(bams : list, index : dict) -> dict:
    scr = {}
    for bam in bams:
        if bam in index.keys():
            print(bam + ": " + index[bam])
            if bam not in scr.keys():
                scr[bam] = index[bam]
            else:
                # looks good!!
                print("dup!!!!!!!!!!")
    return scr

def src_genome(scr : dict) -> list:
    src_genome = []
    for name, acc in scr.items():
        src_genome.append(acc)
    return src_genome


def genome_stat(top : str, genomes : list) -> None:
    with open('genome_stat.txt', 'w') as out:
        for genome in genomes:
            path = os.path.join(top, genome, 'merge.fna')

            header = []
            big_str_len = 0.0
            with open(path) as f:
                for line in f:
                    if line.startswith('>'):
                        header.append(line.split(' ')[0])
                    else:
                        big_str_len += len(line.replace('\n', ''))
            hdic = dict(Counter(header))
            dup_lis = [key for key, value in hdic.items() if value > 1] 
            dup_dic = {key : value for key, value in hdic.items() if value > 1} 

            if dup_lis == [] and dup_dic == {}:
                print(genome + ": passed!\t", end = '')
                print("contigs: " + str(len(header)) + "\tavg_len: " + str(big_str_len / len(header)))
                out.writelines(genome + ": passed!\t")
                out.writelines("contigs: " + str(len(header)) + "\tavg_len: " + str(big_str_len / len(header)) + '\n')
            else:
                out.writelines(genome + ': failed!')

def create_working_dir(index : dict, genomes_top : str, bams_top : str, genomes : list, bams : list, out_dir : str) -> None:
    for name, acc in index.items():
        if name in bams:
            bam_dir = os.path.join(bams_top, str(name).replace(' ', '_'), 'VARUS.bam')
            genome_dir = os.path.join(genomes_top, acc, 'merge.fna')
            wdir = os.path.join(out_dir, acc)

            os.mkdir(wdir)
            if os.path.exists(bam_dir):
                os.system("copy %s %s" % (bam_dir, os.path.join(wdir, 'VARUS.bam')))
                if os.path.exists(os.path.join(wdir, 'VARUS.bam')):
                    print(name + ": BAM copy succeeded")
                else:
                    print(name + ": BAM copy failed")
            else:
                print(name + ": BAM failed")

            if os.path.exists(genome_dir):
                # fix header
                fx = header_fixer.fixer()
                fx.fix_contig_name(genome_dir, genome_dir.replace('merge.fna', 'merge_fix.fna'))
                print("header fixed!")

                os.system("copy %s %s" % (genome_dir.replace('merge.fna', 'merge_fix.fna'), os.path.join(wdir, 'merge_fix.fna')))
                # if os.path.exists(os.path.join(wdir, 'merge.fna')):
                #     print(name + ": genome copy succeeded")
                # else:
                #     print(name + ": genome copy failed")
            else:
                print(name + ": genome failed")

def header_map(genomes_top : str, genomes : list) -> None:
    with open(r'header_map.txt', 'w') as out:
        for genome in genomes:
            gen_path = os.path.join(genomes_top, genome, 'merge.fna')
            # print(gen_path)    
            if os.path.exists(gen_path):
                with open(gen_path) as f:
                    for line in f:
                        if line.startswith('>'):
                            out.writelines(line)
        out.writelines('\n')
    pass

genomes = get_genomes(genomes_top)
bams = get_bams(bams_top)
index = build_index(report_all)
scr = indexing(bams, index)
scr_genome = src_genome(scr)

# genome_stat(genomes_top, scr_genome)
# header_map(genomes_top, scr_genome)

create_working_dir(index, genomes_top, bams_top, genomes, bams, r'D:\working_dir_header_fix')


