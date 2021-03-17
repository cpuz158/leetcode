class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        x1, x2 = 0, 1
        for i in range(len(s)):
            if i-x2 >= 1 and s[i-x2-1:i+1] == s[i-x2-1:i+1][::-1]:
                x1 = i-x2-1
                x2 += 2
                continue
            if i-x2 >= 0 and s[i-x2:i+1] == s[i-x2:i+1][::-1]:
                x1 = i-x2
                x2 += 1
        return s[x1:x1+x2]
