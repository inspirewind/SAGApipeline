import os

path = r"D:\__wsl\VARUS\temp"

good_lis = []

def get_good_spes_dirs(path):
    for root, dirs, files in os.walk(path):
        print("root: ", root)
        print("dirs: ", dirs)
        print("files: ", files)
        global good_lis
        good_lis = dirs
        break

get_good_spes_dirs(path)
with open('good_species.txt', 'w') as out:
    for spe in good_lis:
        out.writelines(str(spe) + '\n')