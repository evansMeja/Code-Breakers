class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                out.append("FizzBuzz")
            else:
                if i % 3 == 0:
                    out.append("Fizz")
                else:
                    if i % 5 == 0:
                        out.append("Buzz")
                    else:
                        out.append(str(i))
                        
        return out
                        
        
