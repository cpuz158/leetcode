class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[0]
        word = ""
        for i in range(len(s)):
            rng = range(i, len(s))
            if len(palindrome) > len(rng):
                break
            for j in rng:
                word += s[j]
                if word == word[::-1] and len(word) > len(palindrome):
                    palindrome = word
            word = ""
        return palindrome
