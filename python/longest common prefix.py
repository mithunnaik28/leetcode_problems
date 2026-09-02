class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare=strs[0]
        for i in range(len(strs)):
            compare1=""
            for j in range(min(len(compare), len(strs[i]))):
                if  strs[i][j] == compare[j]:
                    compare1 += strs[i][j]
                else: 
                    break
            compare=compare1
        return compare
