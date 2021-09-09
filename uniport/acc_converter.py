import os

class acc_converter:
    def __init__(self, db) -> None:
        self.db = db
        self.db_seq = {}

    def makedb(self, output = False):
        with open(self.db) as f:
            # >tr|A0A2P6V1S1|A0A2P6V1S1_9CHLO Sodium potassium calcium exchanger 1 isoform X5 OS=Micractinium conductrix OX=554055 GN=C2E20_8329 PE=3 SV=1
            for line in f:
                if line.startswith('>'):
                    acc = line.split('|')[2].split(' ')[0]
                    pr_os_index = line.find('OS=')
                    pr_ox_index = line.find('OX=')
                    pr_os = line[pr_os_index : pr_ox_index - 1]
                    # print(acc + " : " + pr_os)

                    self.db_seq[acc] = pr_os
            if output == True:
                with open(r'uniprot_index.tsv', 'a') as out:
                    for acc, pr_os in self.db_seq.items():
                        out.writelines(acc + '\t' + pr_os + '\n')

    def get_os(self, acc):
        self.makedb()
        return self.db_seq[acc]

    def get_os_by_traverse(self, acc):
        # maybe faster when inquiry single seq
        with open(self.db) as f:
            for line in f:
                if line.startswith('>'):
                    db_acc = line.split('|')[2].split(' ')[0]
                    pr_os_index = line.find('OS=')
                    pr_ox_index = line.find('OX=')
                    pr_os = line[pr_os_index : pr_ox_index - 1]
                    if acc == db_acc:
                        return pr_os
                    # print(acc + " : " + pr_os)


if __name__ == '__main__':
    ac = acc_converter(r'D:\plantdatabase\Uniprot\uniprot-reviewed_no+taxonomy_3041.fasta')
    ac.makedb(output=False)

    # print(ac.get_os('A0A2P6VGR9_9CHLO'))
    # print(ac.get_os_by_traverse('A0A2P6VGR9_9CHLO'))
    # print(ac.db_seq) 