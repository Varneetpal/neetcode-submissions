class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        i = 0
        j = len(A)-1
        A.sort()
        while i <= j:
            temp = A[i][0] + A[j][0]
            if temp == target:
                # return [i, j]
                return [min((A[i][1]), A[j][1]), max(A[i][1], A[j][1])]
            elif temp > target:
                j -= 1
            elif temp < target:
                i += 1

        return []
        