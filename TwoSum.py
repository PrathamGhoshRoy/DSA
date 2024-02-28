
def twoSum(nums: list[int], target: int) -> list[int]:

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return -1

print(twoSum([2,4,5,6,7,8], 11))

