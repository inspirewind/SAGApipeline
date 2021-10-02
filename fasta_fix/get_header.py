from typing import Counter
import time
import os

genomes_top = r'D:\plantdatabase\plants_genome_new\all'
bams_top = r'D:\plantdatabase\BAMs'

#double Name    Common Name Organism_Qualifier  Taxonomy_id	Assembly_Name   Assembly Accession	Source	Annotation	Level	Contig N50	Size	Submission Date	Gene Count	BioProject	BioSample
report_all = r'C:\Users\lr201\code\gene_prediction_pipeline\data_summary.tsv'

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

def create_working_dir(index : dict, genomes_top : str, bams_top : str) -> None:
    pass

genomes = get_genomes(genomes_top)
bams = get_bams(bams_top)
index = build_index(report_all)
print(index)
scr = indexing(bams, index)
print(len(scr))

# print(bams)
# print(len(bams))
# print(genomes_path)




for genome in genomes:
    path = os.path.join(genomes_top, genome, 'merge.faa')

    header = []
    with open(path) as f:
        for line in f:
            if line.startswith('>'):
                header.append(line.split(' ')[0])

for i in header:
    print(i)

hdic = dict(Counter(header))
print(hdic)
print ([key for key,value in hdic.items()if value > 1])  
print ({key:value for key,value in hdic.items()if value > 1}) 