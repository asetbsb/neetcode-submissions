class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        firstStr = ''.join(sorted(s1))
        L = 0

        for R in range(len(s1)-1, len(s2)):
            newStr = ""
            left = L
            for _ in range(len(s1)):
                newStr += s2[left]
                left += 1
            newStr = ''.join(sorted(newStr))
            if newStr == firstStr:
                return True
            L += 1
            
        return False

