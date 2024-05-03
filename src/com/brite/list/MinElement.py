nums = [3, 2, 4, 1, 5, 7]

nums = sorted(nums)
print(nums[0])

nums = [3, 2, 4, 1, 5, 7]
nums.sort()
print(nums[0])

nums = [3, 2, 4, 1, 5, 7]
minvalue = min(nums)
print(minvalue)

nums = ['3', '2', '4', '1', '5', '7']
minvalue = min(nums, key=int)
print(minvalue)

letters = ['A', 'B', 'C', 'X', 'Y', 'Z']
letter = min(letters)
print(letter)

letter = min([letter.lower() for letter in letters])
print(letter)
