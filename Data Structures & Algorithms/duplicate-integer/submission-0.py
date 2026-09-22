class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        if nums is None:
            return False
        
        if len(nums) == 0:
            return False

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                return True
            i = i + 1

        return False