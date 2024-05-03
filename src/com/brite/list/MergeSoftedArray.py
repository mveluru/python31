import math


def removenumber(integers):
    integers
    print(integers)


m = [1, 2, 3, 0, 0, 0]
removenumber(m)


def removezero(x):
    return x != 0


list_elements = [items for items in m if removezero(items)]
print(list_elements)

list_elements = ['001', '002', '003', '004', '005']
list_elements = [items.strip('0') for items in list_elements]
print(list_elements)

list_elements = []

for item in range(1, 10):
    list_elements.append(item)
print(list_elements)

nums = [3, 2, 2, 3]
val = 3
nums = [e for e in nums if e != val]
print(nums)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
new_nums = []
for item in nums:
    if item != val:
        new_nums.append(item)
print(len(new_nums))

print("*sorted*")
print(sorted(nums))


nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(list(set(nums)))
print(int(math.pow(10, 2)))
