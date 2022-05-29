import os
import shutil
from tqdm import tqdm

final_ass_top = r'F:\final_results'
tar_top = r'E:\final_results_tar'
ass_lis = os.listdir(final_ass_top)

bar_ass_lis = tqdm(ass_lis)
for ass in bar_ass_lis:
    shutil.make_archive(os.path.join(tar_top, ass), 'gztar', final_ass_top, ass)
    bar_ass_lis.set_description(f'ass: {ass}')

