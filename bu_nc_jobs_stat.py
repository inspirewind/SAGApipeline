import os
import pathlib

top = r'D:\new_ncbi_dataset\genome_rec_nc\genomes_rec_Rfam'
ass_lis_tmp = os.listdir(top)
ass_lis = []
for ass in ass_lis_tmp:
    if os.path.isdir(os.path.join(top, ass)):
        ass_lis.append(ass)


for ass in ass_lis:
    Rfam_result_lis = ['.cmscan', '.tblout']
    tRNA_result_lis = ['.out', '.ss', '.stats']
    full_res_lis = Rfam_result_lis + tRNA_result_lis

    for res in Rfam_result_lis + tRNA_result_lis:
        # full_res_lis is global, using + operator to make generator get a new list
        res_path = os.path.join(top, ass, str(ass + res))
        # print(res_path)
        if os.path.exists(res_path):
            # print(f'{ass} {res}')
            full_res_lis.remove(res)

    
    if full_res_lis:
        print(f'{ass}: missing {full_res_lis}')
        pass
    else:
        # print(f'{ass}: validate!')
        pass

    # for result in Rfam_result_lis:
    #     result_path = os.path.join(top, ass, str(ass + result))
    #     if os.path.exists(result_path):
    #         Rfam_result_lis.remove(result)
    # if Rfam_result_lis:
    #     print(f'{ass}: missing {Rfam_result_lis}')
    # else:
    #     print(f'{ass}: validate! [Rfam]', end=',')
            
    # for result in tRNA_result_lis:
    #     result_path = os.path.join(top, ass, str(ass + result))
    #     if os.path.exists(result_path):
    #         tRNA_result_lis.remove(result)
    # if tRNA_result_lis:
    #     print(f' missing {tRNA_result_lis}')
    # else:
    #     print(' [tRNA]')