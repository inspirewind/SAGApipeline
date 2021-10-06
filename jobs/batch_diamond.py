import os

db = r'/mnt/d/plantdatabase/Uniprot/agales/algae_mix_6_92.dmnd'
aa_top = r'/mnt/d/plantdatabase/Uniprot/aa_rec'
aa_lis = os.listdir(aa_top)

if os.name == 'posix':
    print("os.name is posix, can be performed")
    for aa_pre in aa_lis:
        aa_pre_path = os.path.join(aa_top, aa_pre)
        os.system("diamond blastp -q %s -d %s -o %s.tsv" % (aa_pre_path, db, aa_pre.replace('_augustus.ab_initio.aa', '_dia.tsv')))
