import os
import sys

if os.name != 'posix':
    print("check your os!")
    sys.exit(1)

class name_fixer():
    def __init__(self, top) -> None:
        self.top = top
        self.genomes = os.listdir(top)
        # print(self.genomes)

    def rename(self):
        if os.name == 'posix':
            print("os.name is posix, can be performed")
            for genome in self.genomes:
                genome_path = os.path.join(self.top, genome)
                aa_path = os.path.join(genome_path, "braker")
                os.system("echo 'pwd: %s'" % (aa_path))
                os.system("cd %s && if [ -f augustus.ab_initio.aa ]; then mv augustus.ab_initio.aa %s_augustus.ab_initio.aa; echo '%s renamed!'; fi" % (aa_path, genome, genome))
        else:
            print("OsError!")





nf = name_fixer(r'/public/home/yaohuipeng/gene_pre/snakemake/genome')
nf.rename()