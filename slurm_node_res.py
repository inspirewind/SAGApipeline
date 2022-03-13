# resolve how many nodes are avaliable from "scontrol show node" 
import re
import subprocess


res = subprocess.check_output('scontrol show node', shell = True)
res = res.decode('utf-8')

slurm_node_re = re.compile(r'NodeName=(.+) Arch=x86_64 CoresPerSocket=\d+\n {3}CPUAlloc=(\d+) CPUErr=(\d+) CPUTot=(\d+) CPULoad=.+\n(.+\n){3,5}   RealMemory=(\d+) AllocMem=(\d+) FreeMem=(.+) Sockets=.+ Boards=.+\n(.+\n)   Partitions=(.+)')

node_lis = slurm_node_re.findall(res)
for node in node_lis:
    node_info = str(node[0]) + "    \tCPU:" + str(int(node[3])-int(node[2])-int(node[1])) \
        + " \tfree mem:" + str(int(int(node[7]) / 1024)) + ",    \t" + str(node[9])
    print(node_info)

