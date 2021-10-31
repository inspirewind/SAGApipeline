import sys, os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_path)
sys.path.append(base_path)

import get_header

genomes_top = r'D:\working_dir_header_fix'
genomes = get_header.get_genomes(genomes_top)

print(genomes)