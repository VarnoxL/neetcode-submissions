class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        
        while l < r:
            #the shorter wall determines the height
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            max_area = max(max_area, a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


           
    #time O(n)
    #Space O(1)

        