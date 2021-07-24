import pandas as pd
import os
import get_dir_by_acc as gdba

# place the script in 'data' dir
# genus
#   -ncbi_dataset
#       - data
#           -GCA_000000
#           ...
#           -get_name_with_fna.py
#           -data_summary.tsv


data_path = gdba.data_path_passer()
data_sum = os.path.join(data_path, r'data_summary.tsv')

tsv_read = pd.read_csv(data_sum, sep = '\t')
ex = tsv_read[['Organism Scientific Name', 'Assembly Accession']]

def get_fna_path():
    pass

with open('species_for_examine.txt', 'w') as out:
    for row in ex.itertuples():
        double_name = row[1]
        acc = row[2]
        
        print(gdba.get_dir(acc))

        # out.writelines(str(double_name) + '\t' + str(acc) + '\n')
