# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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
    # print(new_array)
    mutate_list(new_array)
    print_list = cut_list(new_array)
    # print(print_list)

    with open(endfile, 'w') as w:
        for i in print_list:
            w.write(str(i))
            w.write('\n')


def mutate_list(new_array: list) -> None:
    """
    Mutate line such that its amino acid codes are 1-digit long instead of 3-digits.
    """
    for i in range(len(new_array) - 1):
        if new_array[i][0] == '...':
            start = new_array[i - 1][0:4]
            if new_array[i][1] in AcidCode:
                end = AcidCode[new_array[i][1]] + new_array[i][2][0:3]
            else:
                end = new_array[i][1] + new_array[i][2][0:3]
        elif new_array[i][0] in AcidCode:
            start = AcidCode[new_array[i][0]] + new_array[i][1][0:3]
            if new_array[i][4] in AcidCode:
                end = AcidCode[new_array[i][4]] + new_array[i][5][0:3]
            else:
                end = new_array[i][4] + new_array[i][5][0:3]
        else:
            start = new_array[i][0] + new_array[i][1][0:3]
            if new_array[i][4] in AcidCode:
                end = AcidCode[new_array[i][4]] + new_array[i][5][0:3]
            else:
                end = new_array[i][4] + new_array[i][5][0:3]
        # line = {start: end}
        line = start + ',' + end
        new_array[i] = line


def cut_list(new_array: list) -> list:
    """
    Return a new list from the values of new_array such that the new list contains no repetitions.
    """
    print_list = []
    keys = []
    # breakpoint()
    for x in new_array:
        if x[0:4] not in keys:
            print_list.append(x)
            keys.append(x[0:4])
        else:
            val = keys.index(x[0:4])
            if x[5:] not in print_list[val]:
                print_list[val] = print_list[val] + x[4:]
    return print_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
