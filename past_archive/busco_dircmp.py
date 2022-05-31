import filecmp
import os
from collections import defaultdict
from sys import argv
from tqdm import tqdm

def compareDirs(d1,d2):
    files1 = defaultdict(set)
    files2 = defaultdict(set)
    subd1  = set()
    subd2  = set()
    for entry in os.scandir(d1):
        if entry.is_dir(): subd1.add(entry)
        else: files1[os.path.getsize(entry)].add(entry)
    # Collecting first to compare length since we are guessing no
    # match is more likely. Can compare files directly if this is
    # not true.
    for entry in os.scandir(d2):
        if entry.is_dir(): subd2.add(entry)
        else: files2[os.path.getsize(entry)].add(entry)

    # Structure not the same. Checking prior to content.
    if len(subd1) != len(subd2) or len(files1) != len(files2): return False

    for size in files2:
        for entry in files2[size]:
            for fname in files1[size]: #If size does not exist will go to else
                if filecmp.cmp(fname,entry,shallow=False): break
            else: return False
            files1[size].remove(fname)
            if not files1[size]: del files1[size]
        
    # Missed a file
    if files1: return False

    # This is enough since we checked lengths - if all sd2 are matched, sd1
    # will be accounted for.
    for sd1 in subd1:
        for sd2 in subd2:
            if compareDirs(sd1,sd2): break
        else: return False # Did not find a sub-directory
        subd2.remove(sd2)

    return True

e_busco = r'E:\genomes_rec_busco'
d_busco = r'D:\new_ncbi_dataset\genomes_rec_busco'

print(compareDirs(e_busco, d_busco))