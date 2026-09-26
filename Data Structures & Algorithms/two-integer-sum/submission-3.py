class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictIndex = {}
        for i in range(len(nums)):
            dictIndex[nums[i]] = i

        nums.sort()

        i = 0
        j = len(nums)-1

        while i <= j:
            if nums[i] + nums[j] == target:
                # return [i, j]
                return [dictIndex[nums[i]], dictIndex[nums[j]]]
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1

        return []
        