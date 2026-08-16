from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = []
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        s1.extend(s2)
        freq = Counter(s1)
        for i in freq:
            if freq[i] == 1:
                s.append(i)
        return s
        