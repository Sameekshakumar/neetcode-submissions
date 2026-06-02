class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_water = 0
        while l<r:
            breadth = min(height[l], height[r])
            length = r-l
            area = breadth*length
            max_water = max(area, max_water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water