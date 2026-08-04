class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            a = i[::-1]
            if i == a:
                return i
        return ""
        