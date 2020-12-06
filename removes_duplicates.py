class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            c = nums.count(i)
            if c > 1:
                while c  != 1:
                    nums.remove(i)
                    c -= 1
        return len(nums)
