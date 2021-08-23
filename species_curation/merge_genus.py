import os
import get_name_with_dir as gnwd
database = r'D:\plants_genome_new'


dep = 0
lis_genus = []
for top, dirs, files in os.walk(database):
    # global lis_genus
    if dep == 0:
        lis_genus = dirs
        dep += 1
        continue
    
    # a genus : ncbi_dataset; README.md
    if dep == 1:
        dep += 1
        continue

    # genus/data
    if dep == 2:
        dep += 1
        continue
    
    # genus/data/GCA ...
    if dep == 3:
        sum_file = os.path.join(top)
        gnwd.get_spe_from_sum(1, sum_file)
        dep += 1
        continue
    
    if dep == 4:
        continue

