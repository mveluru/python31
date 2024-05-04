
list = ['q', 'a', 's', 'd', 'f', 'g', 'q', 'a', 's', 'd', 'c', 'v', 'q', 'a', 's']

uniquelist = []
dupset: set[str] = set()
uniqueueset: set[str] = set()

for item in list:
    if item in uniquelist:
        dupset.add(item)
    else:
        uniquelist.append(item)

for item in uniquelist:
    uniqueueset.add(item)

print(uniqueueset.difference(dupset))

# print(char.difference(dupset))
