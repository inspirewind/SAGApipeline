import pandas as pd
import os
import merge_fna

# place the script in 'data' dir
# genus
#   -ncbi_dataset
#       - data
#           -GCA_000000
#           ...
#           -get_name_with_fna.py
#           -data_summary.tsv

data_path = ""
all_path = r'C:\Users\lr201\code\gene_prediction_pipeline\species_curation\test_data'

def get_dir(acc : str):
    single_path = os.path.join(data_path, acc)
    return single_path

def get_spe_from_sum(mode, path):
    # for dirs
    if mode == 1:
        data_path = path
        data_sum = os.path.join(data_path, r'data_summary.tsv')
    
    #for data_summary_merge.tsv in dir "all"
    if mode == 2:
        data_sum = os.path.join(all_path, "data_summary_merge.tsv")

    tsv_read = pd.read_csv(data_sum, sep = '\t')
    ex = tsv_read[['Organism Scientific Name', 'Assembly Accession']]

    with open('species_for_examine.txt', 'a') as out:
        for row in ex.itertuples():
            double_name = row[1]
            acc = row[2]
            
            fnas_path = get_dir(acc)

            # merge fnas
            merge_fna.merge_fna(merge_fna.get_merge_lis(fnas_path), fnas_path)

            # write to species_for_examine.txt
            out.writelines(str(double_name) + "; " + fnas_path + '\n')

get_spe_from_sum(2, all_path)