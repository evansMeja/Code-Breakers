from itertools import zip_longest
class Solution:    
    def isIsomorphic(self,a, b):
        return len(set(a)) == len(set(b)) == len(set(zip_longest(a, b)))
