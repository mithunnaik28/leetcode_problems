class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        for i in range(len(knowledge)):
            s_m = f"({knowledge[i][0]})"
            find_k = s.find(s_m)
            if find_k >= 0:
                s = s.replace(s_m,knowledge[i][1])
        while s.find("(") >= 0:
            start = s.find("(")
            end = s.find(")")
            value = s[start + 1:end]
            s = s.replace(f"({value})","?")
        return s
        
