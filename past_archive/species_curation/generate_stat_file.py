import os
import xlrd, xlwt

data_path = r'E:\plants_genome_new\all'


def get_fna(genome_path : str):
    pass

def merge_fna(files : list, path) -> None:
    merge_path = os.path.join(path, 'merge.fna')
    with open(merge_path, 'w') as f:
        for file in files:
            single_fna_path = os.path.join(path, file)
            for line in open(single_fna_path):
                f.writelines(line)
    f.close()

def remove_merge(path):
    merge_file  = os.path.join(path, 'merge.txt')
    print("merge_remove!")
    print(str(merge_file))
    os.remove(merge_file)


def fna_files_stat(data_path):
    dic = {}
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('sheet1')

    # root = genus\ncbi_dataset\data
    root = data_path
    i = 1
    for top, dirs, files in os.walk(root):
        print('top:'+ str(top) + '\ndirs:' + str(dirs) + '\nfiles' + str(files))

        # write acc -> 0
        worksheet.write(i, 0, label = str(top).split('\\')[-1])

        # write files_count -> 1
        worksheet.write(i, 1, label = str(len(files)))

        # write fna -> 2
        fna_lis = []
        for file in files:
            if 'fna' in str(file):
                fna_lis.append(file)
        worksheet.write(i, 2, label = str(fna_lis))
        # merge_fna(fna_lis, top)
        # remove_merge(top)

        # write protein.faa -> 3
        if 'faa' not in str(files):
            worksheet.write(i, 3, label = 'NO pro')
        else:
            worksheet.write(i, 3, label = 'protein.faa')

        #write genomic.gbff -> 4
        if 'gbff' not in str(files):
            worksheet.write(i, 4, label = 'NO gbff')
        else:
            worksheet.write(i, 4, label = 'genomic.gbff')

        # write genomic.gff -> 5
        if 'gff' not in str(files):
            worksheet.write(i, 5, label = 'NO gff')
        else:
            worksheet.write(i, 5, label = 'genomic.gff')

        # write genomic.gtf -> 6
        if 'gtf' not in str(files):
            worksheet.write(i, 6, label = 'NO gtf')
        else:
            worksheet.write(i, 6, label = 'genomic.gtf')
        i += 1

    workbook.save('files_stat.xls')

fna_files_stat(data_path)

    

