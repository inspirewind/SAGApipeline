import os
from tqdm import tqdm
from shutil import make_archive

result_opt_top = r'D:\new_ncbi_dataset\result_optimize'

def optimize_braker_ep():
    pass


def optimize_braker_es():
    pass


def optimize_busco(busco_output_dir, ass, mode):
    real_output_dir = None
    for top in os.listdir(busco_output_dir):
        if 'busco' in top and 'snakemake' not in top:
            real_output_dir = os.path.join(busco_output_dir, top)
    
    if real_output_dir is None:
        print('No busco real output dir found')

    for dir in os.listdir(real_output_dir):
        if dir == 'blast_db':
            dst_dir_path = os.path.join(result_opt_top, 'busco', ass, mode)
            if not os.path.exists(dst_dir_path):
                os.makedirs(dst_dir_path)
            src_dir_path = os.path.join(real_output_dir, dir)
            dst_file_path = os.path.join(dst_dir_path, 'blast_db')
            make_archive(dst_file_path, 'gztar', src_dir_path,)
            


        # elif 'run' in dir:
        #     with tarfile.open(os.path.join(top, dir), 'r:gz') as tar:
        #         for file in os.listdir(os.path.join(real_output_dir, dir)):
        #             tar.add(os.path.join(real_output_dir, dir, file))

def main():
    busco_test_top = r'D:\new_ncbi_dataset\genomes_rec_busco\done\done_busco_genome_lCh_aupCr_Chlorophyte_3041'
    ass_lis = os.listdir(busco_test_top)
    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
    bar_ass_lis = tqdm(ass_lis)
    for ass in bar_ass_lis:
        busco_output_dir = os.path.join(busco_test_top, ass, 'busco_output_dir')
        optimize_busco(busco_output_dir, 'genome', ass)



if __name__ == '__main__':
    main()