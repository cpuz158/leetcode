class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        length = 0
        for x in s:
            if x in sub:
                length = max(length, len(sub))
                sub = sub[sub.index(x)+1:]
            sub.append(x)
        return max(length, len(sub))
