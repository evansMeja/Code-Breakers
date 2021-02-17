class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        missing = 0
        missingDetected = False
        for i in range(0, len(nums)):
            if nums[i] != i:
                missing = i
                missingDetected = True
                break
        if missingDetected:
            return missing
        else:
            return len(nums)
                
        
                
