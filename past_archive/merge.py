#!/usr/bin/python3
import re
import os
get_gene = r'(# start gene g\d+\n(.+\n)+?###)'
get_cds = r'(\[.+\n(.+\n)+?.+])|(\[.+\n.+])|(\[.+])'
global gene_cnt
gene_cnt = 1
out = open('merge.fasta', 'w')

#将文件读取到bigstr中
# def GetFileFromThisRootDir(dir,ext = ".fna.masked"):
#   allfiles = []
#   needExtFilter = (ext != None)
#   for root,dirs,files in os.walk(dir):
#     for filespath in files:
#       filepath = os.path.join(root, filespath)
#       extension = os.path.splitext(filepath)[1][1:]
#       if needExtFilter and extension in ext:
#         allfiles.append(filepath)
#       elif not needExtFilter:
#         allfiles.append(filepath)
#   return allfiles
file_name = r'output.gff'

def split_to_sixty(cds):
    new = str()
    cnt = 0
    for i in cds:
        if cnt < 60:
            new += i
            cnt +=1
        else:
            new += '\n'
            cnt = 0
    new += '\n'
    return new

def single_file_cds_output(file_name, output_stream):
    with open(file_name, encoding='utf-8') as f:
        bigstr = ""
        for line in f:
            bigstr += line

    #我也不知道正则表达式咋写的，能用就行吧，有时间系统学下
    gene = re.findall(get_gene, bigstr)

    global gene_cnt
    for i in gene:
        #好像search匹配到一个就返回，具体没搞懂，先能用就行吧
        cds_tmp = re.search(get_cds, str(i[0])).group()
        cds_real = cds_tmp.replace('\n# ', '').replace('[', '').replace(']', '')
        # print(cds_real)
        output_stream.writelines('>' + str(gene_cnt) +'\n')
        output_stream.writelines(split_to_sixty(cds_real))
        gene_cnt += 1
        


def trv_dir():
    # global gene_cnt
    gene_cnt = 1
    cur_dir = os.path.abspath('.')
    contig_top = os.path.join(cur_dir, 'contig_output')
    for root, dirs, files in os.walk(contig_top):
        for f in files:
            single_file_cds_output(os.path.join(contig_top, f), out)
            # gene_cnt += 1

def main():
    # trv_dir()
    single_file_cds_output(file_name, out)


if __name__ == '__main__':
    main()