class Solution:     
    def reverse(self, x: int) -> int:
        l=str(x)
        s=0
        if l[0] == "-":
            s = s + int("-"+l[1:][::-1])
        else:
            s = s + int(l[0:][::-1])
        return 0 if (abs(s) > ((1 << 31))) else s
