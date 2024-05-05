import math


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

nums = {0, 1, 2, 2, 3, 0, 4, 2}
print("Directly adding set to list")
print(list(set(nums)))

print(int(math.pow(10, 2)))
