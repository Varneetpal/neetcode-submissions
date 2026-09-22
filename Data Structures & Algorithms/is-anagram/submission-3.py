class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictS = {} # O(26) and hence O(1) space comp because 
                   # the string only contains lowercase letters
                   # and hence there are only 26 possibilities and
                   # 26 is a constant
        dictT = {}

        for i in s: # O(n) time comp
            if i in dictS:
                dictS[i] = dictS[i] + 1
            else:
                dictS[i] = 1

        for i in t: # O(n) time comp
            if i in dictT:
                dictT[i] = dictT[i] + 1
            else:
                dictT[i] = 1

        if dictS == dictT:
            return True

        return False