class Solution:
    def maxArea(self, height: List[int]) -> int:
        b = 0
        f= 0
        l = len(height) -1
        
        while f < l:
            
            if height[f] < height[l]:
                area = height[f] * (l - f)
                f += 1
                
            else:
                area = height[l] * (l - f)
                l -= 1
                
            if area > b:
                b = area
                
        return b
