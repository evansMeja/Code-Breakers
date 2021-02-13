class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return nums1
        nums1[-(len(nums2)):]=nums2
        return nums1.sort()
        
