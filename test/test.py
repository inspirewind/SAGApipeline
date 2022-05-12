# def a():
#     def b():
#         return "i'm b"
#     print(b())
# a()

import os

# with open(r'C:\Users\lr201\code\gene_prediction_pipeline\test\fna_stat.txt', 'r') as f:
#     lis = f.readlines()
#     print(len(lis))


linux_path = 'mnt/d'
win_path = r'gene_prediction_pipeline\test'

print(os.path.join(linux_path, win_path))