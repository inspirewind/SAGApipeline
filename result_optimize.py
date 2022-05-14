import os
from tqdm import tqdm
from shutil import make_archive, copy

result_opt_top = r'D:\new_ncbi_dataset\result_optimize'

def optimize_braker_ep():
    pass


def optimize_braker_es():
    pass


def optimize_busco(ass_path, mode, type):
    # ass/
    #  - busco_output_dir/
    #     - .snakemake_timastamp
    #     - real_output_dir/
    #        - blast_db
    #        - logs
    #        - run_{lineage_database}
    
    busco_var_dir = [x for x in os.listdir(os.path.join(ass_path, 'busco_output_dir')) if 'busco' in x][0]
    real_output_dir = os.path.join(ass_path, 'busco_output_dir', busco_var_dir)
    
    if real_output_dir is None:
        print('No busco real output dir found')
    
    tar_lis = [tar for tar in os.listdir(real_output_dir) if 'run' in tar]
    if mode == 'genome' and (type == 'LCA' or type == 'recommend'):
        tar_lis.append('blast_db')

    if type == 'auto':
        tar_lis.append('auto_lineage')
    
    tar_lis.append('logs')

    ass = os.path.basename(ass_path)
    for dir in tar_lis:
        dst_path = os.path.join(result_opt_top, ass, 'busco', mode)
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        dst_file = os.path.join(dst_path, dir)
        src_path = os.path.join(real_output_dir, dir)
        if not os.path.exists(dst_file + '.tar.gz'):
            # make_archive(dst_file, 'gztar', src_path)
            pass
        else:
            print('Already exists: {}'.format(dst_file))
            
    # TODO: add remaining files
    remaining_file_lis = set(os.listdir(real_output_dir)) - set(tar_lis)
    for file in remaining_file_lis:
        dst_path = os.path.join(result_opt_top, ass, 'busco', mode)
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        dst_file = os.path.join(dst_path, file)
        src_path = os.path.join(real_output_dir, file)
        if not os.path.exists(dst_file):
            copy(src_path, dst_file)



def main():
    busco_test_top = r'D:\new_ncbi_dataset\genomes_rec_busco\genome\LCA\done_busco_genome_lCh_aupCr_Chlorophyte_3041'
    ass_lis = os.listdir(busco_test_top)
    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
    bar_ass_lis = tqdm(ass_lis)
    for ass in bar_ass_lis:
        ass_path = os.path.join(busco_test_top, ass)
        optimize_busco(ass_path, 'genome')



if __name__ == '__main__':
    main()