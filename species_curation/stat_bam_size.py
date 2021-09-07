import os
from tsv_reader import tsv_reader

species_path = r"D:\plantdatabase\BAMs"
tsv_path = r"data_summary_merge.tsv"
tr = tsv_reader(tsv_path)

# for top, dirs, files in os.walk(bam_path):
#     pass

ex_dic = {}

with open("bam_stat.tsv", "w") as out:
    for sp in os.listdir(species_path):
        bam_path = os.path.join(species_path, sp, "VARUS.bam")
        name = sp.replace("_", " ")
        acc = str(tr.name2acc(name))

        if os.path.exists(bam_path):
            bam_size = os.path.getsize(bam_path)
            out.writelines(name + '\t' + str(round(bam_size / 1024**2, 2)) + 'MB\t' + acc + "\n")
        else:
            out.writelines(name + '\t' + "NO BAM!" + '\t' + acc + "\n")
        


# print(os.listdir(bam_path))