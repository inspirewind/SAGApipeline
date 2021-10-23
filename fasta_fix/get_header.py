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


def genome_stat(top : str, genomes : list, output = False) -> None:
    genome_stat_lis = []
    
    for genome in genomes:
        path = os.path.join(top, genome, 'merge.fna')
        headers = []
        header_len_lis = []
        big_str_len = 0.0

        with open(path) as f:
            header_len = 0
            for line in f:
                if line.startswith('>'):
                    header_len_lis.append(header_len)
                    header_len = 0
                    headers.append(line.split(' ')[0])
                else:
                    big_str_len += len(line.replace('\n', ''))
                    header_len += len(line.replace('\n', ''))
        del(header_len_lis[0])

        #test contig dup
        hdic = dict(Counter(headers))
        dup_lis = [key for key, value in hdic.items() if value > 1] 
        dup_dic = {key : value for key, value in hdic.items() if value > 1} 
        avg_len = float(big_str_len) / float(len(headers))

        if dup_lis == [] and dup_dic == {}:
            genome_stat_lis.append((genome, len(headers), avg_len, max(header_len_lis), min(header_len_lis)))
        else:
            print(genome + ': failed!')

        genome_stat_lis = sorted(genome_stat_lis, key = lambda x : x[2], reverse = True)
        # print(genome_stat_lis)

    if output:
        long_mi = []
        short_mi = []
        with open('genome_stat.txt', 'w') as out:
            for genome_pair in genome_stat_lis:
                genome = genome_pair[0]
                contigs = genome_pair[1]
                avg_len = genome_pair[2]
                max_len = genome_pair[3]
                min_len = genome_pair[4]

                if avg_len > 1e5:
                    long_mi.append(genome)
                else:
                    short_mi.append(genome)

                print(genome, end = '')
                print("\tcontigs: " + str(contigs) + "\tavg_len: " + str(avg_len))
                out.writelines(genome)
                out.writelines("\tcontigs: " + str(contigs) + "\tavg_len: " + str(avg_len))
                out.writelines("\tmax = " + str(max_len) + "\tmin =  " + str(min_len) + '\n')
        print(long_mi)
        print(short_mi)

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

genome_stat(genomes_top, scr_genome, output = True)
# header_map(genomes_top, scr_genome)

# create_working_dir(index, genomes_top, bams_top, genomes, bams, r'D:\working_dir_header_fix')


