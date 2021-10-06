import evalue_verify
from blast_resolver import blast_resolver
import os

blast_dir = r'D:\plantdatabase\Uniprot\aa_rec\diamond'

blast_lis = os.listdir(blast_dir)
# print(aa_lis)

for aa_pre in blast_lis:
    print(aa_pre)
    pre_blastdb = evalue_verify.make_pre_blast_db(os.path.join(blast_dir, aa_pre))
    evalue_db = evalue_verify.get_best_evalue(pre_blastdb)
    evalue_verify.verify(evalue_db)
    print()