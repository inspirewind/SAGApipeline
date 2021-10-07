#!/bin/bash
#SBATCH -p com
#SBATCH -N 2
#SBATCH -c 32
#export PATH=/public/software/apps/Anaconda/envs/gene_pre/bin/:$PATH
snakemake -s ab_initio.smk --cores 64 --jobs 8 --keep-going