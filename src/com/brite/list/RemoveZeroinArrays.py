m = [1, 2, 3, 0, 0, 0]


def removezero(x):
    return x != 0


list_elements = [items for items in m if removezero(items)]
print(list_elements)
