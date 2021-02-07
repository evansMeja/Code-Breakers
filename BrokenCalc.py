class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        if X>=Y:
            return X-Y
        else:
            result = 0
            while Y>X:
                if Y%2==1:
                    result += 1
                    Y+=1
                result += 1
                Y//=2
            result += X-Y
            return result
