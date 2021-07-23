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
        species[(line.split('\t')[0])] = line.split('\t')[1]

with open('good_species.txt', 'w') as out:
    for name, acc in species.items():
        if has_two_word(name) and exclude_sp(name):
            out.writelines(name + '; ' + with_dir(acc))

# for i in species:
#     if len(i.split(' ')) == 2:
#         print(str(len(i.split(' '))) + ': ' + i)