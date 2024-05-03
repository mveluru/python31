from functools import reduce

dupsnums = set()
uniquenums = set()

##nums = [2, 3, 4, 5, 6, 2, 3, 8, 4]
# nums = [2, 3, 4, 5, 6, 2, 3, 8, 4, 2, 3, 4]
nums = [13, 13, 1, 13, 14]


def dupelements(nums):
    for item in nums:
        if item in uniquenums:
            dupsnums.add(item)
        else:
            uniquenums.add(item)


def removerepeatedelement():
    for item in dupsnums:
        uniquenums.remove(item)


def sumelement(numsa):
    values = reduce(lambda x, y: x + y, numsa)
    return values


def adduniqueelement(nums):
    dupelements(nums)
    removerepeatedelement()


adduniqueelement(nums)
sum_value = sumelement(uniquenums)
print(sum_value)



# print(uniquenums)
# print()
# print(dupsnums)
