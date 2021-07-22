import time
import threading



# def hello(name):
#     while 1:
#         print("hello",name)
#         time.sleep(3)

# hello("c137-max")
# print("end")


filename = ''
seq = {}

cnt = 1
with open(r'seq.fna') as f:
    for line in f:
        if line.startswith('>'):
            name = line
            seq[name] = ''
            print('contig: ' + str(cnt))
            cnt += 1
        else:
            seq[name] += line

sort_seq = sorted(seq.items(), key = lambda x: len(x[1]))
# print(seq)
with open(r'stat_mut.txt', 'w') as out:
    for k, v in sort_seq:
        out.writelines(k.replace('\n', '') + '\t' + str(len(v.replace('\n', ''))) + '\n')
# read()
# write()
print('finish!')