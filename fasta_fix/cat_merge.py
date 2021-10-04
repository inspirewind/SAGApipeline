import os
import sys

# if os.name != 'posix':
#     sys.exit(1)

class cater():
    def __init__(self, top) -> None:
        self.top = top
        self.genomes = os.listdir(top)
        print(self.genomes)

    def cat(self):
        if os.name == 'posix':
            print("os.name is posix, can be performed")
            for genome in self.genomes:
                genome_path = os.path.join(self.top, genome)
                os.system("echo 'pwd: %s'" % (genome_path))
                os.system("cd %s && if [ -f rna.fna ]; then mv rna.fna rna.f_n_a.donotmerge; echo 'rna has masked!'; fi" % (genome_path))
                os.system("cd %s && cat *.fna > merge.fna && echo '%s merged!'" % (genome_path, genome_path))
        else:
            print("OsError!")
    
    def remove(self):
        if os.name == 'posix':
            print("os.name is posix, can be performed")
            for genome in self.genomes:
                genome_path = os.path.join(self.top, genome)
                os.system("echo 'pwd: %s'" % (genome_path))
                os.system("cd %s && rm -f merge.fna && echo '%s removed!'" % (genome_path, genome_path))
        else:
            print("OsError!")


c = cater(r'/mnt/d/plantdatabase/plants_genome_new/all')
c.cat()
