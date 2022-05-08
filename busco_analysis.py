import os
from busco_resolver import busco_resolver

busco_top = r'D:\new_ncbi_dataset\genome_rec_busco'
part_lis = os.listdir(os.path.join(busco_top, 'done'))
lineage_dic = {'Eu': 'eukaryota', 'St': 'stramenopiles', 'Vi': 'viridiplantae', 'Al': 'alveolata', 'Eg': 'euglenozoa', 'Ch': 'chlorophyta'}

def target_res(path):
    target_lis = path.split('_')

    mode = target_lis[2]
    busco_lineage = target_lis[3].replace('l', '')
    augustus_species = target_lis[4].replace('aup', '')
    ass_lineage = target_lis[5]
    taxid = target_lis[6]
    return mode, busco_lineage, augustus_species, ass_lineage, taxid

for part in part_lis:
    if 'done' in part:
        part_path = os.path.join(busco_top, 'done', part)
        target_lis = target_res(part)
        ass_lis = os.listdir(part_path)
        for ass in ass_lis:
            if 'GCA' in ass:
                ass_path = os.path.join(part_path, ass)
                busco_output_path = os.path.join(ass_path, 'busco_output_dir')

                try:
                    output = os.listdir(busco_output_path)[0]
                    if 'busco' not in output:
                        output = os.listdir(busco_output_path)[1]
                    busco_summary_path = os.path.join(busco_output_path, output, f'run_{lineage_dic[target_lis[1]]}_odb10', 'short_summary.txt') 
                    busco_res = busco_resolver(busco_summary_path)
                    # print(f'ass: {ass}, busco_count: {busco_res.busco_count}, lineage: {lineage_dic[target_lis[1]]}')
                    if target_lis[0] == 'genome':
                        print(f'{ass}, ' + ('%.2f' % busco_res.busco_count) + f', {lineage_dic[target_lis[1]]}_genome')
                    elif target_lis[0] == 'protein':
                        print(f'{ass}, ' + ('%.2f' % busco_res.busco_count) + f', {lineage_dic[target_lis[1]]}_protein')
                    else:
                        print("WARNING: target_lis[0] is not 'genome' or 'protein'")
                except FileNotFoundError:
                    print("No busco output found for {}".format(ass))