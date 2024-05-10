class TwoSum:
    def twoSum(nums: list[int], target: int):
        dictMap = {}
        for item in range(len(nums)):
            dictMap[nums[item]] = item

        for item in range(len(nums)):
            y = target - nums[item]
            if y in dictMap and y != nums[item]:
                print(y, nums[item])


twosumleet = TwoSum

nums = [3, 2, 4]
target = 6

#the following usecase failing
# nums = [3, 3]
# target = 6
##nums = [2, 7, 11, 15]
##target = 9

twosumleet.twoSum(nums, target)
