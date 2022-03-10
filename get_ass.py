import os

genomes = r'D:\new_ncbi_dataset\genomes_rec'
ass_lis = []

lineages = os.listdir(genomes)
# print(lineage)

for li in lineages:
    li_path = os.path.join(genomes, li)
    ass = os.listdir(li_path)
    for a in ass:
        ass_lis.append(str(li) + '/' + str(a))
print(ass_lis)
# print(len(ass_lis))
