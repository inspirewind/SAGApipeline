import os
from tqdm import tqdm
from shutil import make_archive, copy

busco_top = r'E:\genomes_rec_busco'
result_opt_top = r'E:\new_ncbi_dataset\result_optimize'
mode_lis = ['genome', 'protein']
strategy_lis = ['LCA', 'recommend', 'auto']


def optimize_braker_ep():
    pass
def optimize_braker_es():
    pass

def optimize_busco(ass_path, mode, strategy):
    # ass/
    #  - busco_output_dir/
    #     - .snakemake_timastamp
    #     - real_output_dir/
    #        - blast_db
    #        - logs
    #        - run_{lineage_database}

    ass = os.path.basename(ass_path)
    busco_var_dir = None
    real_output_dir = None

    if any("busco" in s for s in os.listdir(ass_path)):
        first_var = [x for x in os.listdir(os.path.join(ass_path)) if 'busco' in x][0]
        first_var_path = os.path.join(ass_path, first_var)
        if any('short_summary' in s for s in os.listdir(first_var_path)):
            real_output_dir = first_var_path
            # print(f'{mode}, {strategy}, {real_output_dir}')
        elif '.snakemake_timestamp' in os.listdir(first_var_path):
            second_var_path = [x for x in os.listdir(os.path.join(first_var_path)) if 'busco' in x][0]
            real_output_dir = os.path.join(first_var_path, second_var_path)
            # print(f'{mode}, {strategy}, {real_output_dir}')
        else:
            print(f'{mode}, {strategy}, {ass} find busco output dir error')
            return None
    else:
        print(f'{ass} busco maybe not run')
        return None

    tar_lis = [tar for tar in os.listdir(real_output_dir) if 'run' in tar]
    if mode == 'genome' and (strategy == 'LCA' or strategy == 'recommend'):
        tar_lis.append('blast_db')
    if strategy == 'auto':
        tar_lis.append('auto_lineage')
    tar_lis.append('logs')

    dst_path = os.path.join(result_opt_top, ass, mode, strategy)
    # dst_path = os.path.join(result_opt_top, mode, strategy, ass)
    for dir in tar_lis:
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        dst_file = os.path.join(dst_path, dir)
        src_path = os.path.join(real_output_dir, dir)
        if not os.path.exists(dst_file + '.tar.gz'):
            make_archive(dst_file, 'gztar', src_path)
        else:
            # print('Already exists: {}'.format(dst_file))
            pass
            
    # remaining files that not compress 
    remaining_file_lis = set(os.listdir(real_output_dir)) - set(tar_lis)
    for file in remaining_file_lis:
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        dst_file = os.path.join(dst_path, file)
        src_path = os.path.join(real_output_dir, file)
        if not os.path.exists(dst_file):
            copy(src_path, dst_file)



def main():
    for mode in mode_lis:
        for strategy in strategy_lis:
            run_top = os.path.join(busco_top, mode, strategy) # safe
            # print(f'{os.path.exists(run_top)} {run_top}')

            if strategy == 'auto':
                ass_lis = os.listdir(run_top)
                ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
                print(f'{run_top}, {len(ass_lis)}')
                bar_lis = tqdm(ass_lis)
                for ass in bar_lis:
                    ass_top = os.path.join(run_top, ass)
                    optimize_busco(ass_top, mode, strategy)
                    bar_lis.set_description(f'{mode}_{strategy}, {ass}')

            else:
                part_lis = os.listdir(run_top)
                for part in part_lis:
                    ass_lis = os.listdir(os.path.join(run_top, part))
                    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
                    bar_lis = tqdm(ass_lis)
                    for ass in bar_lis:
                        optimize_busco(os.path.join(run_top, part, ass), mode, strategy)
                        bar_lis.set_description(f'{mode}_{strategy}, {ass}')

if __name__ == '__main__':
    main()