nums = [3, 2, 4, 1, 5, 7]

nums = sorted(nums)
print(nums[len(nums) - 1])

nums = [3, 2, 4, 1, 5, 7, 100]
nums.sort()
print(nums[len(nums) - 1])

nums = [10, 3, 2, 4, 1, 5, 7]
minvalue = max(nums)
print(minvalue)

nums = ['3', '2', '4', '1', '5', '7']
minvalue = max(nums, key=int)
print(minvalue)

letters = ['A', 'B', 'C', 'X', 'Y', 'Z']
letter = max(letters)
print(letter)

letter = max([letter.lower() for letter in letters])
print(letter)
