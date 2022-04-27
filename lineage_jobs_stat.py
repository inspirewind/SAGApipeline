import os
from snakemake_log_resolver import log_path2job
from ncbi_datasets_resolver import resolve_ass_json, get_ass_list_from_json

genomes_rec_part_top = r'D:\new_ncbi_dataset\genomes_rec_part'
part_lis = os.listdir(genomes_rec_part_top)

def validate_job_dic(job_dic, part):
    for ass, jobs in job_dic.items():
        ass_path = os.path.join(genomes_rec_part_top, part, ass)
        braker_path = os.path.join(ass_path, 'braker')
        gtf_path = os.path.join(braker_path, 'braker.gtf')
        ips_path = os.path.join(braker_path, 'interproscan.tsv')
        dia_path = os.path.join(braker_path, 'matches.tsv')

        jobs = list(set(jobs))
        try:
            jobs.remove('star_remove')
        except ValueError:
            print('WARNING: star_remove not in jobs')
        if os.path.exists(gtf_path):
            try:
                jobs.remove('braker2')
            except ValueError:
                print('WARNING: braker2 not in jobs, but braker.gtf exists, this may because of running braker2 without snakemake')
        if os.path.exists(ips_path):
            try:
                jobs.remove('interproscan')
            except ValueError:
                print('WARNING: interproscan not in jobs, but interproscan.tsv exists, this may because of running interproscan without snakemake')
        if os.path.exists(dia_path):
            try:
                jobs.remove('diamond')
            except ValueError:
                print('WARNING: diamond not in jobs, but matches.tsv exists, this may because of running diamond without snakemake')

        if len(jobs) == 0:
            print(f'{ass}: validate! [BRAKER2, INTERPROSCAN, DIAMOND]')
        else:
            print(f'{ass}: missing! {jobs}')


for part in part_lis:
    if 'done_ips_dia' in part:
        print(part)

        # stat all finished ass
        log_path = os.path.join(genomes_rec_part_top, part, '.snakemake', 'log')
        ass_job_dic = log_path2job(log_path)
        validate_job_dic(ass_job_dic, part)

        # stat braker2 failed ass
        genome_store_path = r'D:\new_ncbi_dataset\genomes_store'
        lineage = part.replace('done_ips_dia_', '')
        json_path = os.path.join(genome_store_path, lineage, 'ncbi_dataset', 'data', 'assembly_data_report.jsonl')
        
        ass_list = get_ass_list_from_json(resolve_ass_json(json_path))
        failed_ass = set([ass for ass in ass_list if 'GCF' not in ass]) - set(ass_job_dic.keys())
        print(f'failed_ass: {(failed_ass)}')
        print(f'failed_ass_num: {len(failed_ass)}')


        print()