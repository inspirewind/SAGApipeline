#!/bin/bash
#SBATCH -p com
#SBATCH -c 30
#export PATH=/public/software/apps/Anaconda/envs/gene_pre/bin/:$PATH
snakemake -s ab_initio_8cores.smk --cores 30 --jobs 5 --keep-going --rerun-incomplete