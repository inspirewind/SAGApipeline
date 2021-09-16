from re import T
from blast_resolver import blast_resolver

def make_pre_blast_db(path):
    # replace after test
    path = ''
    br = blast_resolver(r'D:\plantdatabase\Uniprot\fmt6_Ch_re_pre.blast')
    br.make_blastdb()
    return br.blastdb

def get_best_evalue(blastdb : dict):
    evalue_db = {}
    for uni_pr, pair in blastdb.items():
        uni_pr = uni_pr
        pre_pr = pair[0]
        evalue = pair[1]
        if pre_pr not in evalue_db.keys():
            evalue_db[pre_pr] = [evalue]
        else:
            evalue_db[pre_pr].append(evalue)

    return evalue_db

def verify(evalue_db : dict):
    # TODO: make db and out to file, do not rev dirctly
    good_pre = 0
    total_pre = len(evalue_db)
    print(total_pre)
    with open(r"verify.txt", 'w') as out:
        for pr, evalue_lis in evalue_db.items():
            if '0.0' in evalue_lis:
                good_pre += 1
            out.writelines(pr + ": " + min(evalue_lis) + "\n")
    print(good_pre / total_pre)

def main():
    pre_blastdb = make_pre_blast_db('')
    # print(pre_blastdb)
    evalue_db = get_best_evalue(pre_blastdb)
    # print(evalue_db)
    verify(evalue_db)





if __name__ == '__main__':
    main()