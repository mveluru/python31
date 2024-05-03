abc = [4, 5, 1, 3, 100, 8, 10, 11]
n = len(abc)
for i in range(n - 1):
    sortedValue = True
    for j in range(0, n - i - 1):
        if abc[j] > abc[j + 1]:
            sortedValue = False
            abc[j], abc[j + 1] = abc[j + 1], abc[j]

    if sortedValue:
        break
print(abc)
