class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        Outp = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in Outp:
                Outp[key] = []
            Outp[key].append(i)
        return list(Outp.values())
