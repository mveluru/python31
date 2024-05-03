mydict = {}
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
for i in range(len(keys)):
    mydict[keys[i]] = values[i]

for k, v in mydict.items():
    print(k, v)

abc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iteration = iter(abc)
for i in iteration:
    print(i, end=" ")
