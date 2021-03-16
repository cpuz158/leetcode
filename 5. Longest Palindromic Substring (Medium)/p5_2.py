class Solution:
    def longestPalindrome(self, s: str) -> str:
        w = ""
        pal = ""
        for i in range(len(s)):
            w = ""
            j = i
            odd = len(s[i:]) % 2
            for j in range(i, i + len(s[i:]) // 2 + odd):
                w += s[j]
                if w == w[::-1] and len(w) > len(pal):
                    pal = w
            m = w + s[j+1:]
            if m == m[::-1] and len(m) > len(pal):
                pal = m
        return pal
