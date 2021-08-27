from os import path


species = {}

# only using this method can screen well
def has_two_word(line : str):
    if len(line.split(' ')) == 2:
        return True
    return False

def exclude_sp(line : str):
    if 'sp.' in line:
        return False
    return True

def with_dir(acc : str):
    # TODO: with dirs
    return acc

with open('species_for_examine.txt', 'r') as sp:
    for line in sp:
        species[line.split(';')[0]] = (line.split(';')[1].replace(' ', ''))

# print(path_lis)

with open('good_species.txt', 'w') as out:
    for name in species:
        if has_two_word(name) and exclude_sp(name):
            final_path = name + '; ' +  str(species[name]).replace('\n', '') + '\merge.fna' + '\n'

            dir_for_linux = final_path.replace("\\", "/").replace('D:', '~')
            out.writelines(dir_for_linux)

# for i in species:
#     if len(i.split(' ')) == 2:
#         print(str(len(i.split(' '))) + ': ' + i)