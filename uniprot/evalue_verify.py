from re import T
from blast_resolver import blast_resolver
from timer import timer


def make_pre_blast_db(path):
    # replace after test
    br = blast_resolver(path)
    br.make_blastdb()
    return br.blastdb

@timer.timeit
def get_best_evalue(blastdb : dict):
    evalue_db = {}
    for uni_pr, pair in blastdb.items():
        uni_pr = uni_pr
        pre_pr = pair[0]
        evalue = float(pair[1])
        if pre_pr not in evalue_db.keys():
            evalue_db[pre_pr] = [evalue]
        else:
            evalue_db[pre_pr].append(evalue)

    return evalue_db

@timer.timeit
def verify(evalue_db : dict):
    # TODO: make db and out to file, do not rev directly

    good_pre_0 = 0
    good_pre_100 = 0
    good_pre_50 = 0
    good_pre_20 = 0
    good_pre_25 = 0
    good_pre_5 = 0

    total_pre = len(evalue_db)
    print(total_pre)
    with open(r"verify.txt", 'w') as out:
        for pr, evalue_lis in evalue_db.items():
            if float(0.0) in evalue_lis:
                good_pre_0 += 1
            if min(evalue_lis) < float(1e-100):
                good_pre_100 += 1
            if min(evalue_lis) < float(1e-50):
                good_pre_50 += 1
            if min(evalue_lis) < float(1e-25):
                good_pre_25 += 1
            if min(evalue_lis) < float(1e-20):
                good_pre_20 += 1
            if min(evalue_lis) < float(1e-5):
                good_pre_5 += 1
            out.writelines(pr + ": " + str(min(evalue_lis)) + "\n")
    print('full_match_rate: ' + str(float(good_pre_0 / total_pre)))
    print('100_match_rate: ' + str(float(good_pre_100 / total_pre)))
    print('50_match_rate: ' + str(float(good_pre_50 / total_pre)))
    print('25_match_rate: ' + str(float(good_pre_25 / total_pre)))
    print('20_match_rate: ' + str(float(good_pre_20 / total_pre)))
    print('5_match_rate: ' + str(float(good_pre_5 / total_pre)))

def main():
    pre_blastdb = make_pre_blast_db(r'D:\__wsl\gene_pre_2109\snakemake\new_sel\dia_013435795_pre_6_92.tsv')
    # print(pre_blastdb)
    evalue_db = get_best_evalue(pre_blastdb)
    # print(evalue_db)
    verify(evalue_db)





if __name__ == '__main__':
    main()