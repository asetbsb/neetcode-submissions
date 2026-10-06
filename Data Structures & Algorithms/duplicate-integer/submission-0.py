class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            for j, n in enumerate(nums):
                if i==j:
                    continue
                elif nums[i]==nums[j]:
                    return True
        return False
            
        
         