import os
from time import sleep
from busco_resolver import busco_resolver
from ncbi_datasets_resolver import ass2lineage

busco_top = r'D:\new_ncbi_dataset\genomes_rec_busco'
wsl_top = r'/mnt/d/new_ncbi_dataset/final_results'
lineage_dic = {'Eu': 'eukaryota', 'St': 'stramenopiles', 'Vi': 'viridiplantae', 'Al': 'alveolata', 'Eg': 'euglenozoa', 'Ch': 'chlorophyta'}
mode_lis = ['genome', 'protein']
strategy_lis = ['LCA', 'recommend', 'auto']

def get_busco_output_summary(ass_path):
    busco_summary_file = None
    normal_path = os.path.join(ass_path, 'busco_output_dir')
    # if not os.path.exists(normal_path):
    #     
    if os.path.exists(normal_path):
        busco_var_dir = [x for x in os.listdir(os.path.join(normal_path)) if 'busco' in x][0]
        real_output_dir = os.path.join(normal_path, busco_var_dir)

        busco_summary_file = [x for x in os.listdir(real_output_dir) if '.txt' in x][0]
        busco_summary_file = os.path.join(real_output_dir, busco_summary_file)
        if os.path.exists(busco_summary_file):
            # print('looks good!')
            pass
        else:
            print('No busco summary file found: {}'.format(busco_summary_file))
    else: # ass -> busco output var, no busco_output_dir
        abnormal_var = [x for x in os.listdir(os.path.join(ass_path)) if 'busco' in x]
        if len(abnormal_var) != 0:
            abnormal_path = os.path.join(ass_path, abnormal_var[0])
            busco_summary_file = [x for x in os.listdir(abnormal_path) if '.txt' in x][0]
            busco_summary_file = os.path.join(abnormal_path, busco_summary_file)
            if os.path.exists(busco_summary_file):
                # print('looks good!')
                pass
            else:
                # print('No busco summary file found: {}'.format(busco_summary_file))
                return None  
        else: # no busco output var
            # print(f'{ass_path} No busco output dir found')
            # pass
            return None  

    return busco_summary_file

def get_all_count():
    print('mode, strategy, lineage, ass, count, mode_strategy')
    ass_lis = os.listdir(wsl_top)
    for ass in ass_lis:
        ass_path = os.path.join(wsl_top, ass, 'busco')
        for mode in mode_lis:
            for strategy in strategy_lis:
                busco_runs_top = os.path.join(ass_path, mode, strategy)
                if os.path.exists(busco_runs_top):
                    if os.listdir(busco_runs_top) != []:
                        busco_summary_file = [x for x in os.listdir(busco_runs_top) if ('.txt' in x and 'specific' in x)][0]
                        busco_summary = os.path.join(busco_runs_top, busco_summary_file)
                        if busco_summary is not None:
                            count = busco_resolver(busco_summary).busco_count
                            lineage = ass2lineage(ass).split('_')[0]
                            print(f'{mode}, {strategy}, {lineage}, {ass}, {count}, {mode}_{strategy}')
                    else:
                        pass

    


def auto_diff(mode, strategy):
    strategy_runs_top = os.path.join(wsl_top, mode, strategy)
    auto_runs_top = os.path.join(wsl_top, mode, 'auto')
    ass_lis = os.listdir(auto_runs_top)
    ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
    lineage_lis = os.listdir(strategy_runs_top)
    lineage_lis = [lineage for lineage in lineage_lis if 'done' in lineage]

    good, bad, equal = 0, 0, 0
    for auto_ass in ass_lis:
        auto_ass_path = os.path.join(auto_runs_top, auto_ass)

        # for lineage to search ass in strategy_runs_top, it can be optimized after running result_optimize.py
        for lineage in lineage_lis:
            ass_lis = os.listdir(os.path.join(strategy_runs_top, lineage)) 
            ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
            for strategy_ass in ass_lis:
                strategy_ass_path = os.path.join(strategy_runs_top, lineage, strategy_ass)
                if strategy_ass == auto_ass:
                    auto_summary = get_busco_output_summary(auto_ass_path)
                    strategy_summary = get_busco_output_summary(strategy_ass_path)
                    if (auto_summary is not None) and (strategy_summary is not None):
                        auto_count = busco_resolver(auto_summary).busco_count
                        strategy_count = busco_resolver(strategy_summary).busco_count
                        if auto_count - strategy_count > 0.001:
                            # print(f'LCA good! {auto_count}, {strategy_count}')
                            good += 1
                        elif auto_count - strategy_count < -0.001:
                            # print(f'LCA bad! {auto_count}, {strategy_count}')
                            bad += 1
                        elif abs(auto_count - strategy_count) < 0.001:
                            # print(f'LCA equal! {auto_count}, {strategy_count}')
                            equal += 1
    print(f'{mode} {strategy} {good} {bad} {equal}')

        

    

def main():
    get_all_count()
    # auto_diff('genome', 'LCA')

if '__main__' == __name__:
    main()
    
# def get_all_count():
#     print('mode, strategy, lineage, ass, count, mode_strategy')
#     total_num = 0
#     for mode in mode_lis:
#         for strategy in strategy_lis:
#             busco_runs_top = os.path.join(wsl_busco_top, mode, strategy)

#             if strategy != 'auto':
#                 lineage_lis = os.listdir(busco_runs_top)
#                 lineage_lis = [lineage for lineage in lineage_lis if 'done' in lineage]


#                 for lineage in lineage_lis:
#                     ass_lis = os.listdir(os.path.join(busco_runs_top, lineage)) 
#                     ass_lis = [ass for ass in ass_lis if 'GCA' in ass]
#                     # print(f'{mode} {strategy} {lineage} {len(ass_lis)}')
#                     for ass in ass_lis:
#                         ass_path = os.path.join(busco_runs_top, lineage, ass)
#                         busco_summary = get_busco_output_summary(ass_path)
#                         if busco_summary is not None:
#                             count = busco_resolver(busco_summary).busco_count
#                             print(f'{mode}, {strategy}, {lineage}, {ass}, {count}, {mode}_{strategy}')
#                             sleep(0.01)
#                             total_num += 1
            
#             elif strategy == 'auto':
#                 ass_lis = os.listdir(busco_runs_top)
#                 ass_lis = [ass for ass in ass_lis if 'GCA' in ass] 
#                 for ass in ass_lis:
#                     ass_path = os.path.join(busco_runs_top, ass)
#                     busco_summary = get_busco_output_summary(ass_path)
#                     if busco_summary is not None:
#                         count = busco_resolver(busco_summary).busco_count
#                         print(f'{mode}, {strategy}, {lineage}, {ass}, {count}, {mode}_{strategy}')
#                         sleep(0.01)
#                         total_num += 1
    
    
                    
# print(f'total num: {total_num}')
# for part in part_lis:
#     if 'done' in part:
#         part_path = os.path.join(busco_top, 'done', part)
#         target_lis = target_res(part)
#         ass_lis = os.listdir(part_path)
#         for ass in ass_lis:
#             if 'GCA' in ass:
#                 ass_path = os.path.join(part_path, ass)
#                 busco_output_path = os.path.join(ass_path, 'busco_output_dir')

#                 try:
#                     output = os.listdir(busco_output_path)[0]
#                     if 'busco' not in output:
#                         output = os.listdir(busco_output_path)[1]
#                     busco_summary_path = os.path.join(busco_output_path, output, f'run_{lineage_dic[target_lis[1]]}_odb10', 'short_summary.txt') 
#                     busco_res = busco_resolver(busco_summary_path)
#                     # print(f'ass: {ass}, busco_count: {busco_res.busco_count}, lineage: {lineage_dic[target_lis[1]]}')
#                     if target_lis[0] == 'genome':
#                         print(f'{ass}, ' + ('%.2f' % busco_res.busco_count) + f', {lineage_dic[target_lis[1]]}_genome')
#                     elif target_lis[0] == 'protein':
#                         print(f'{ass}, ' + ('%.2f' % busco_res.busco_count) + f', {lineage_dic[target_lis[1]]}_protein')
#                     else:
#                         print("WARNING: target_lis[0] is not 'genome' or 'protein'")
#                 except FileNotFoundError:
#                     print("No busco output found for {}".format(ass))


# def target_res(path):
#     target_lis = path.split('_')

#     mode = target_lis[2]
#     busco_lineage = ('_' + target_lis[3]).replace('_l', '')
#     augustus_species = target_lis[4].replace('aup', '')
#     ass_lineage = target_lis[5]
#     taxid = target_lis[6]
#     return mode, busco_lineage, augustus_species, ass_lineage, taxid