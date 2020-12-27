class Solution:
    def convert(self, s: str, numRows: int) -> str:
        p = -1
        rows = 0
        
        ans = [[] for i in range(numRows)]
        
        if numRows == 1 or len(s) <= numRows:
            return s
        
        for c in s:
            ans[rows].append(c)
            if rows == 0 or rows == numRows - 1:
                p *= -1
            rows += p
            
        for i in range(len(ans)):
            ans[i] = "".join(ans[i])
            
            
        return "".join(ans)
            
