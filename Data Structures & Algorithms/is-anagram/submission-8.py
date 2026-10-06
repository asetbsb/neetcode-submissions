class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDict = dict()
        secondDict = dict()
        
        for i in s:
            if i in firstDict:
                firstDict[i] += 1 
            else:
                firstDict[i] = 1  
        
        for j in t:
            if j in secondDict:
                secondDict[j] += 1  
            else:
                secondDict[j] = 1  

        print(firstDict, " | ", secondDict)
        
        return firstDict == secondDict
        