class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictStrs = {}

        for i in range(len(strs)):
            strTemp = strs[i]
            sorted(strs[i])
            key = "".join(sorted(strs[i]))

            if key in dictStrs:
                dictStrs[key].append(strTemp)
            else:
                dictStrs[key] = [strTemp]

        strs.clear()

        for key in dictStrs:
            strs.append(dictStrs[key])

        return strs




