import os
import sys

# if os.name != 'posix':
#     print("check your os!")
#     sys.exit(1)

class name_fixer():
    def __init__(self, top) -> None:
        self.top = top
        self.genomes = os.listdir(top)
        # print(self.genomes)
    
    def rename(self, file : str) -> None:
        pass

    def aa_in_braker_rename(self):
        if os.name == 'posix':
            print("os.name is posix, can be performed")
            for genome in self.genomes:
                genome_path = os.path.join(self.top, genome)
                aa_path = os.path.join(genome_path, "braker")
                os.system("echo 'pwd: %s'" % (aa_path))
                os.system("cd %s && if [ -f augustus.ab_initio.aa ]; then mv augustus.ab_initio.aa %s_augustus.ab_initio.aa; echo '%s renamed!'; fi" % (aa_path, genome, genome))
        else:
            print("OsError!")

    def busco_rename(self):
        bu_lis = os.listdir(r'/mnt/c/Users/lr201/code/gene_prediction_pipeline/jobs/busco_summary')
        for bu_summary in bu_lis:
            print(bu_summary)
            # os.system('mv short_summary.specific.chlorophyta_odb10.GCA_008729055.1_augustus.ab_initio.aa.busco.txt')
    
    def rename_raker_log(self):
        if os.name == 'posix':
            print("os.name is posix, can be performed")
            for genome in self.genomes:
                genome_path = os.path.join(self.top, genome)
                aa_path = os.path.join(genome_path, "braker")
                # print(genome_path)
                os.system("echo 'pwd: %s'" % (aa_path))
                os.system("cd %s && if [ -f braker.log ]; then cp braker.log ../%s_braker.log; echo '%s renamed!'; fi" % (aa_path, genome, genome))
        else:
            print("OsError!")


nf = name_fixer(r'/public/home/yaohuipeng/gene_pre/snakemake/pr_working_dir_header_fix')
# nf.rename()
# nf.busco_rename()
nf.braker_log_rename()