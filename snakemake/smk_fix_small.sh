#!/bin/bash
#SBATCH -p com
#SBATCH -n 8
#SBATCH -c 8
#export PATH=/public/software/apps/Anaconda/envs/gene_pre/bin/:$PATH
snakemake -s ab_initio_header_fix.smk --cores 64 --jobs 8 --keep-going --rerun-incomplete