class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        stringLength = len(s)
        longestString = 0
        for i in range(0,stringLength):
            testString = s[i:]
            f=[]
            c = 0
            string = ''
            y = 0
            for x in testString:
                if x in f:
                    string = testString[:c]
                    y = 1
                    break
                f.append(x)
                c = c + 1
            if y != 1:
                string = testString

            if len(string) > longestString:
                longestString = len(string)
            c = c

        return longestString
