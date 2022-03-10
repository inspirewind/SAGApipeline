from re import T
from blast_resolver import blast_resolver
from timer import timer


def make_pre_blast_db(path):
    # replace after test
    br = blast_resolver(path)
    br.make_blastdb()
    return br.blastdb

# @timer.timeit
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

def make_evalue_dic(*args) -> dict:
    res_dic = {}
    for i in sorted(list(args)):
        res_dic[i] = 0
    return res_dic

# @timer.timeit
def verify(evalue_db : dict):
    # TODO: make db and out to file, do not rev directly
    evalue_dic = make_evalue_dic(200, 100, 50, 25, 5)

    total_pre = len(evalue_db)
    print(total_pre)

    with open(r"verify.txt", 'w') as out:
        good_pre_0 = 0
        for pr, evalue_lis in evalue_db.items():
            if float(0.0) in evalue_lis:
                good_pre_0 += 1
            for ev in evalue_dic.keys():
                if min(evalue_lis) < float(10**(-ev)):
                    evalue_dic[ev] += 1
            out.writelines(pr + ": " + str(min(evalue_lis)) + "\n")

    print('full_match_rate: ' + str(float(good_pre_0 / total_pre)))
    for ev in evalue_dic.keys():
        print('%d_match_rate: ' % (ev) + str(float(evalue_dic[ev])/total_pre))


def main():
    pre_blastdb = make_pre_blast_db(r'D:/plantdatabase/Uniprot/fmt_6_Ch_re_protein.blast')
    evalue_db = get_best_evalue(pre_blastdb)
    verify(evalue_db)

    

if __name__ == '__main__':
    main()