#!/bin/bash
#SBATCH -p com
#SBATCH -N 2
#SBATCH -c 30
#export PATH=/public/software/apps/Anaconda/envs/gene_pre/bin/:$PATH
snakemake -s ep_6cores.smk --cores 60 --jobs 10 --keep-going --rerun-incomplete