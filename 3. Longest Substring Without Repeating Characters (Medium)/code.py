class Solution_1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = []  # memory for storing characters
        l = 0   # the longest length ever
        for c in s:
            if c in m:
                l = max(l, len(m))
                m = m[m.index(c)+1:]
            m.append(c)
        return max(l, len(m))


class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = l = 0
        for j, c in enumerate(s):
            if c in s[i:j]:
                l = max(l, len(s[i:j]))
                i += s[i:j].index(c) + 1
        return max(l, len(s[i:j+1]))

s1 = Solution_1()
print(s1.lengthOfLongestSubstring("abcabcbb"))
print(s1.lengthOfLongestSubstring("bbbbb"))
print(s1.lengthOfLongestSubstring("pwwkew"))

s2 = Solution_2()
print(s2.lengthOfLongestSubstring("abcabcbb"))
print(s2.lengthOfLongestSubstring("bbbbb"))
print(s2.lengthOfLongestSubstring("pwwkew"))