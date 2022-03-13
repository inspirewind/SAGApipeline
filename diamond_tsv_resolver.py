import decimal
import statistics
import pandas as pd

matches = pd.read_csv('test/matches.tsv', sep = '\t')

def remove_zero(x):
    if x != 0:
        return x
    else:
        return None

e_value_lis = matches['e_value']
# e_value_lis = list(map(remove_zero, list(matches['e_value'])))
# e_value_lis = e_value_lis[1:20000]

dec_evalue_lis = []

def add_header():
    pass

for evalue in e_value_lis:
    if evalue is not None:
        dec_evalue_lis.append(decimal.Decimal(evalue))

print(len(dec_evalue_lis))
dec_am = statistics.mean(dec_evalue_lis)
print(dec_am)

# float_evalue_lis = []
# for fl in e_value_lis:
#     float_evalue_lis.append(float(fl))

# float_gm = statistics.geometric_mean(float_evalue_lis)
# dec_gm = statistics.geometric_mean(dec_evalue_lis)
# print('fgm: ' + str(float_gm))
# print('dgm: ' + str(dec_gm))
# print(float_gm == dec_gm)

