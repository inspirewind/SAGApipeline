import os

def merge_fna(files : list, path) -> None:
    merge_path = os.path.join(path, 'merge.fna')
    with open(merge_path, 'w') as f:
        for file in files:
            single_fna_path = os.path.join(path, file)
            for line in open(single_fna_path):
                f.writelines(line)
    f.close()

def get_merge_lis(path):
    fna_lis = []
    for top, dirs, files in os.walk(path):
        for file in files:
            if 'fna' in str(file):
                fna_lis.append(file)
    return fna_lis

def cat_merge():
    
    os.system("cat *.fna > merge.fna")
