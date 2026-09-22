class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numsSet = set() # space comp is O(n)

        for i in range(len(nums)):  # time comp O(n)
            if nums[i] in numsSet: # O(1) for hash
                return True
            numsSet.add(nums[i])
        
        return False



        # nums.sort()   ------------- nlogn time comp
        #### Space comp can be O(1) because not creating any
        #### new/auxilary data structure but can be using internal
        #### memomy so O(n) in the worst case scenario 

        # if nums is None:
        #     return False
        
        # if len(nums) == 0:
        #     return False

        # i = 0
        # while i < len(nums) - 1:  --------------  O(n) time comp
        #     if nums[i] == nums[i+1]:
        #         return True
        #     i = i + 1

        # return False