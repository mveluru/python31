import itertools


def substring(string):
    stringset = set()
    my_list = [1, 2, 3, 4, 5]
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if string[i:j] != '':
                stringset.add(string[i:j])
    return sorted(stringset)


print(substring('johnsmith'))


def allsubstring(string):
    stringset = set()
    for i in range(len(string)):
        for combination in itertools.combinations(string, i):
            stringset.add(''.join(combination))

    return stringset


print(sorted(allsubstring('john')))