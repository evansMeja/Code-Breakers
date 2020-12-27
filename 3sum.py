class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
           
            
            while l < r:
                summation = nums[i] + nums[l] + nums[r]
                if summation < 0:
                    l += 1
                elif summation > 0:
                    r -= 1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    
                    while(l < r and nums[l] == nums[l + 1]):
                        l += 1
                    
                    while(l < r and nums[r] == nums[r - 1]):
                          r -= 1
                        
                    l += 1
                    r -= 1
            
                
        return ans
