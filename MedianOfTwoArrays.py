class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for n in nums2:
            nums1.append(n)
        
        nums1.sort()
        
        
        if len(nums1) % 2 == 0:
            mid1 = len(nums1) // 2
            mid2 = mid1 -1
            
            s = float(nums1[mid1] + nums1[mid2])
            return s / 2
        else:
            md = len(nums1) // 2
            return nums1[md]
            
