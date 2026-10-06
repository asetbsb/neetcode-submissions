class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maximum = 0

        while right>left:
            distance = right - left
            leftElement, rightElement = heights[left], heights[right]

            if leftElement>rightElement:
                area = distance*rightElement
                if area>maximum:
                    maximum = area
                right -= 1
            else:
                area = distance*leftElement
                if area>maximum:
                    maximum = area
                left += 1
                
        return maximum
            
