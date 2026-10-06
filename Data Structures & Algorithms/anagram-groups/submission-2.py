class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedS = ""
        res = dict()

        for s in strs:
            for i in sorted(s):
                sortedS += i
            if sortedS not in res:
                res[sortedS] = []
            res[sortedS].append(s)
            sortedS = ""
        
        return res.values()

            


            

        