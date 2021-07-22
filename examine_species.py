species = []

def has_two_word(line : str):
    if len(line.split(' ')) == 2:
        return True
    return False

def exclude_sp(line : str):
    pass

# def 

with open('species_for_VARUS.txt', 'r') as sp:
    for line in sp:
        species.append(line.split('\t')[0])


for i in species:
    if len(i.split(' ')) == 2:
        print(str(len(i.split(' '))) + ': ' + i)