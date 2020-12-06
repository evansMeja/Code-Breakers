class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:return False
        n=x
        l = []
        while n != 0:
            l = [n % 10] + l
            n = n // 10
        l=l[::-1]
        u=len(l)-1
        i=0
        f=0
        while i <= u:
            f = f + pow(10,(u-i)) * l[i]
            i = i + 1    
        return True if f == x else False
