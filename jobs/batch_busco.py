import os

aa_top = r'/mnt/d/com_esmode/protein'
aa_lis = os.listdir(aa_top)
busco_rec = r'/mnt/d/com_esmode/protein/busco_rec'

if os.name == 'posix':
    print("os.name is posix, can be performed")
    for aa_pre in aa_lis:
        aa_pre_path = os.path.join(aa_top, aa_pre)
        # print(aa_pre_path)
        os.system("busco -i %s --offline -l /mnt/d/plantdatabase/busco_downloads/lineages/chlorophyta_odb10 -o %s.busco -m proteins -c 8" % (aa_pre_path, aa_pre))
