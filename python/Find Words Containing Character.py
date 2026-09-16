class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result_list = []
        for i in range(len(words)):
            if words[i].find(x) != -1:
                result_list.append(i)
        return result_list
