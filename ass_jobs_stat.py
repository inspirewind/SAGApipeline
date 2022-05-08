from math import ceil
import os
import re
from dateutil.parser import parse
from ncbi_datasets_resolver import resolve_ass_json, get_ass_list_from_json

genomes_rec_part_top = r'D:\new_ncbi_dataset\genomes_rec_part'
braker_log_re = re.compile(r'# (.+): braker.pl version 2.1.6\n(.+\n)+# (.+): deleting job lst files \(if existing\)')

def get_time_from_log(log_path):
    with open(log_path, 'r') as f:
        big_str = f.read()
        time_pair = braker_log_re.findall(big_str)
        time = ceil((parse(time_pair[0][2]) - parse(time_pair[0][0])).total_seconds() / 60)
        return time

# json_path = os.path.join(genome_store_path, lineage, 'ncbi_dataset', 'data', 'assembly_data_report.jsonl')

def jobs_stat(genomes_rec_part_top):
    jobs_stat_dic = {}
    part_lis = os.listdir(genomes_rec_part_top)
    print(part_lis)


    for part in part_lis:
        if 'done' in part:
            ass_lis = os.listdir(os.path.join(genomes_rec_part_top, part))
            ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
            print(f'{part}: {len(ass_lis)}')

            well_done_lis = [] # finish braker2, interproscan, diamond
            fail_lis = [] # because of ips and dia depends on braker2's protein, failed jobs' flag_lis is None
            incomplete_lis = []

            for ass in ass_lis:
                ass_path = os.path.join(genomes_rec_part_top, part, ass)
                braker_path = os.path.join(ass_path, 'braker')
                braker_log_path = os.path.join(braker_path, 'braker.log')
                
                gtf_path = os.path.join(braker_path, 'braker.gtf')
                ips_path = os.path.join(braker_path, 'interproscan.tsv')
                dia_path = os.path.join(braker_path, 'matches.tsv')

                flag_lis = []
                if os.path.exists(gtf_path):
                    flag_lis.append('braker2')
                if os.path.exists(ips_path):
                    flag_lis.append('interproscan')
                if os.path.exists(dia_path):
                    flag_lis.append('diamond')
                if os.path.exists(braker_log_path):
                    time = get_time_from_log(braker_log_path)
                    # print(f'{ass}: {time}')

                if {'braker2', 'interproscan', 'diamond'} == set(flag_lis):
                    well_done_lis.append(ass)
                elif len(flag_lis) == 0:
                    fail_lis.append(ass)
                else:
                    incomplete_lis.append((ass))
                    # incomplete_lis.append((ass, flag_lis))

            jobs_stat_dic[part] = {'well_done_lis': well_done_lis, 'fail_lis': fail_lis, 'incomplete_lis': incomplete_lis} 
            
            # jobs_stat_dic[part] = {'well_done_lis': len(well_done_lis), 'fail_lis': len(fail_lis), 'incomplete_lis': len(incomplete_lis)}         
            # print(f'{part}: done: {len(well_done_lis)}')
            # print(f'{part}: failed: {len(fail_lis)}')
            # print(f'{part}: inc: {incomplete_lis}')

    return jobs_stat_dic

def main():
    jobs_stat_dic = jobs_stat(genomes_rec_part_top)
    for part, stat in jobs_stat_dic.items():
        print(f'{part}: stats: {stat}')


if __name__ == '__main__':
    main()       