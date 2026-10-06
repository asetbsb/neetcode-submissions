class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnList = list()
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    product *= nums[j]
            returnList.append(product)
            product = 1
        
        return returnList

            