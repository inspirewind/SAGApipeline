import os
import re
from functools import reduce
from acc_converter import acc_converter
from timer import timer

without_sp_and_more_than_two = []
bad_name = []
remain = []

class os_resolver:
    pass

class blast_resolver:
    # @timer.timeit
    def __init__(self, blast) -> None:
        self.os_lis = []
        self.blastdb = {}
        self.osdb = {}
        self.blast = blast

    # @timer.timeit
    def make_blastdb(self, output = False):
        # lcl|NC_005353.1_prot_NP_958375.1_1	tr|A0A6C0RXD1|A0A6C0RXD1_9CHLO	99.201	751	6	0	1	751	1	751	0.0	1520
        # query_acc; subject_acc; identity; ali_len; mismatches; gap opens; q.start; q.end; s.start; s.end; e-value; bit_score
        with open(self.blast) as f:
            for line in f:
                split_lis = line.split('\t')
                query_acc = split_lis[0]
                subject_acc = split_lis[1]
                e_value = split_lis[10]
                self.blastdb[subject_acc] = (query_acc, e_value)
                # print(query_acc + " " + subject_acc + " " + e_value)

        if output == True:
            pass
    
    def os_fix(os_name : str):
        global without_sp_and_more_than_two
        global bad_name
        global remain

        os_words = os_name.split(' ')
        if len(os_words) > 2:
            if "sp." not in os_words and 'subsp.' not in os_words:
                fix_name = os_words[0] + " " + os_words[1]
                without_sp_and_more_than_two.append(fix_name)
                return fix_name
                # print(os_name + " -> " + fix_name)
            elif "sp." in os_words:
                if bool(re.search(r'\d', os_name)) or not "a".islower():
                    bad_name.append(os_name)
                elif "'" in os_name and (len(os_words) - 2) == 1 and [x + x for x in os_words[1 : -1]]:
                    fix_name = os_name.replace("'", "")
                    return fix_name
                else:
                    remain.append(os_name)
            else:
                remain.append(os_name)
        else:
            # good name
            return os_name

        # with open(r'a') as out:
        #     pass
    
    def out_fix_log():
        # TODO: three list or more to output
        pass

    # @timer.timeit
    def make_osdb(self, os_lis = [], prdb = None, output = False):
        # list for indpecting pr_os name, then write to file
        # ins_set = set()

        ac = acc_converter(prdb)

        # test_lis
        # os_lis = ['Dunaliella tertiolecta']
        if os_lis == []:
            os_lis = self.os_lis
            # print(self.os_lis)

        ac.makedb(output = False)
        for subject_acc, info_pair in self.blastdb.items():
            sub_acc_fix = subject_acc.split('|')[2]
            pr_os = ac.get_os(sub_acc_fix).replace('OS=', '')

            #inspect os name
            # ins_set.add(pr_os)
            pr_os_fix = blast_resolver.os_fix(pr_os)
            # print(pr_os)
            if pr_os_fix in os_lis:
                self.osdb[subject_acc] = (info_pair[0], info_pair[1], pr_os_fix)
        
        # inspect
        # with open(r"os_name_ins.txt", 'w') as out:
        #     for i in ins_set:
        #         out.writelines(str(i) + '\n')

        if output == True:
            with open(r'os_ref.blast', 'w') as out:
                for sub, pair in self.osdb.items():
                    out.writelines(sub + "\t" + pair[0] + "\t" + pair[1] + "\t" + pair[2] + "\n")

        print(len(self.osdb))

    def os_reader(self, path):
        with open(path) as f:
            for line in f:
                self.os_lis.append(line.replace('\n', ''))
        print("os number: " + str(len(self.os_lis)))



if __name__ == '__main__':
    br = blast_resolver(r'D:/plantdatabase/Uniprot/fmt_6_Ch_re_protein.blast')
    br.make_blastdb()
    br.os_reader(r'os.txt')
    br.make_osdb(prdb = r'D:\plantdatabase\Uniprot\uniprot-reviewed_no+taxonomy_3041.fasta', output = True)

    # print("without_sp_and_than_two: " + str(without_sp_and_more_than_two))
    # print("bad_name: " + str(bad_name))
    # print("remain: " + str(remain))

    # test_str = "aaa bbb ccc"
    # a = test_str.split(' ')
    # print(len(a))
    # print(a[1 : -1])