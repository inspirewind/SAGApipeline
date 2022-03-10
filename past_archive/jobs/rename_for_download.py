import os
import sys
from argparse import ArgumentParser

def run(cmd):
    os.system(cmd)
    
def rename(top : str, file : str) -> None:
    genomes = os.listdir(top)
    for genome in genomes:
        genome_path = os.path.join(top, genome, 'braker')
        file_path = os.path.join(genome_path, file)
        cmd = (
            f'echo "renaming: {file_path}" && '
            f'cd {genome_path} && '
            f'if [ -f {file} ]; then cp {file} {top}/{genome}_{file}; '
            f'echo "{file_path} renamed!"; '
            f'fi'
        )
        run(cmd)

def busco_rename(self):
    bu_lis = os.listdir(r'/mnt/c/Users/lr201/code/gene_prediction_pipeline/jobs/busco_summary')
    for bu_summary in bu_lis:
        print(bu_summary)


parser = ArgumentParser(description = "Renaming ")
parser.add_argument('--dir', '-d', type = str, help = "Specify the directory to be renamed, note that this directory contains every genome folder")
parser.add_argument('--file_name', '-f', type = str, help = "the file you want to rename")

args = parser.parse_args()

if __name__ == "__main__":
    rename(args.dir, args.file_name)

# nf = name_fixer(r'/public/home/yaohuipeng/gene_pre/snakemake/pr_working_dir_header_fix')
# nf.rename()
# nf.busco_rename()
# nf.braker_log_rename()