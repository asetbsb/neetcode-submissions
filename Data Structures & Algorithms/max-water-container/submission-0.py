class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i==j:
                    continue
                distance = abs(j-i)
                first = heights[i]
                second = heights[j]

                if first>second:
                    area = distance*second
                else:
                    area = distance*first

                if area>maxArea:
                    maxArea = area
                
        return maxArea
            
