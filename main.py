# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pprint

AcidCode = {
    'Ala': 'A', 'Arg': 'R', 'Asn': 'N', 'Asp': 'D', 'Cys': 'C', 'Gln': 'Q', 'Glu': 'E', 'Gly': 'G',
    'His': 'H', 'Ile': 'I', 'Leu': 'L', 'Lys': 'K', 'Met': 'M', 'Phe': 'F', 'Pro': 'P', 'Ser': 'S',
    'Thr': 'T', 'Trp': 'W', 'Tyr': 'Y', 'Val': 'V'
}

def read_file(filename: str, endfile: str) -> None:
    """
    Read filename and then write endfile.
    """
    new_array = []
    with open(filename) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            new_array.append(lines[i].split())
    mutate_list(new_array)
    print_list = cut_list(new_array)
    sort_horiz(print_list)
    sort_vert(print_list)

    endfile = endfile
    with open(endfile, 'w') as w:
        w.write('source atoms,target atoms--')
        w.write('\n')
        for i in print_list:
            w.write(str(i))
            w.write('\n')


def mutate_list(new_array: list) -> None:
    """
    Mutate new_array such that its amino acid codes are 1-digit long instead of 3-digits,
        unnecessary information has been removed, and each element is in a csv formatting.
    """
    for i in range(len(new_array)):
        if new_array[i][0] == '...':
            index = new_array[i - 1].find(',')
            start = new_array[i - 1][0:index]
            if new_array[i][1] in AcidCode:
                end = AcidCode[new_array[i][1]] + new_array[i][2][0:-1]
            else:
                end = new_array[i][1] + new_array[i][2][0:-1]
        elif new_array[i][0] in AcidCode:
            start = AcidCode[new_array[i][0]] + new_array[i][1][0:-1]
            if new_array[i][4] in AcidCode:
                end = AcidCode[new_array[i][4]] + new_array[i][5][0:-1]
            else:
                end = new_array[i][4] + new_array[i][5][0:-1]
        else:
            start = new_array[i][0] + new_array[i][1][0:-1]
            if new_array[i][4] in AcidCode:
                end = AcidCode[new_array[i][4]] + new_array[i][5][0:-1]
            else:
                end = new_array[i][4] + new_array[i][5][0:-1]
        line = start + ',' + end
        new_array[i] = line


def cut_list(new_array: list) -> list:
    """
    Return a new list from the values of new_array such that the new list contains no repetitions.
    """
    print_list = []
    keys = []
    for x in new_array:
        index = x.find(',')
        if x[0:index] not in keys:
            print_list.append(x)
            keys.append(x[0:index])
        else:
            val = keys.index(x[0:index])
            if x[index + 1:] not in print_list[val]:
                print_list[val] = print_list[val] + x[index:]
    return print_list


def sort_horiz(print_list: list) -> None:
    """
    Mutate print_list such that each target value is sorted by its numerical code.
    """
    for j in range(len(print_list)):
        s = str(print_list[j])
        line = s.split(',')
        n = len(line)
        for i in range(0, n):
            for k in range(1, n - i - 1):
                if int(line[k][1:]) > int(line[k + 1][1:]):
                    line[k], line[k + 1] = line[k + 1], line[k]
        s = str.join(',', line)
        print_list[j] = s


def sort_vert(print_list: list) -> None:
    """
    Mutate print_list such that each column is sorted by the numerical code of its first value.
    """
    for i in range(len(print_list)):
        index = print_list[i].find(',')
        for j in range(len(print_list) - 1):
            if int(print_list[j][1:index]) > int(print_list[j + 1][1:index]):
                print_list[j], print_list[j + 1] = print_list[j + 1], print_list[j]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
