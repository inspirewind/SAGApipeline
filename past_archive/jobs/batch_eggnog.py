import os

cds_top = r'/mnt/d/com_esmode/cds'
cds_lis = os.listdir(cds_top)
# print(cds_lis)
eggnog_rec = r'/mnt/d/com_esmode/eggnog_rec'

if os.name == 'posix':
    print("os.name is posix, can be performed")
    for cds in cds_lis:
        cds_path = os.path.join(cds_top, cds)
        # print(aa_pre_path)
        os.system(f"emapper.py -m diamond --itype CDS -i {cds_path} --output {cds} --output_dir {eggnog_rec} --cpu 8 -d euk")
