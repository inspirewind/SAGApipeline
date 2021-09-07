import pandas as pd

class tsv_reader:

    def __init__(self, path) -> None:
        self.ex_dic = {}
        self.path = path
        self.tsv_read = pd.read_csv(path, sep = '\t')
        self.ex = self.tsv_read[['Organism Scientific Name', 'Assembly Accession']]
        
        for row in self.ex.itertuples():
            double_name = row[1]
            acc = row[2]
            self.ex_dic[acc] = double_name

    def acc2name(self, acc):
        return self.ex_dic[acc]

    def name2acc(self, name):
        rev = {v : k for k, v in self.ex_dic.items()}
        return rev[name]


if __name__ == '__main__':
    tsv_path = r"data_summary_merge.tsv"
    tr = tsv_reader(tsv_path)
    print(tr.acc2name("GCA_000818905.1"))
    print(tr.name2acc("Trebouxia gelatinosa"))



# ex = tsv_read[['Organism Scientific Name', 'Assembly Accession']]