class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = float("-inf")
        window = set()

        for R in range(len(s)):
            if s[R] in window:
                while s[R] in window:
                    window.remove(s[L])
                    L += 1
            length = max(length, R - L + 1)
            window.add(s[R])
        
        return 0 if length == float("-inf") else length