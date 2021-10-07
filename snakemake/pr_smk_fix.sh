#!/bin/bash
#SBATCH -p com
#SBATCH -n 2
#SBATCH -c 32
#export PATH=/public/software/apps/Anaconda/envs/gene_pre/bin/:$PATH
snakemake -s with_pr_header_fix.smk --cores 64 --jobs 8 --keep-going --rerun-incomplete