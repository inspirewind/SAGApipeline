import os
import shutil

top = r'/mnt/d/new_ncbi_dataset/genomes_rec'
snakemake_rec = r'/mnt/d/new_ncbi_dataset/genomes_rec_snakemake'

lineages = os.listdir(top)
for lineage in lineages:
    ass_lis = os.listdir(os.path.join(top, lineage))
    for ass in ass_lis:
        shutil.copytree(os.path.join(top, lineage, ass), os.path.join(snakemake_rec, ass))