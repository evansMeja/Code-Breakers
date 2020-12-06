"""
validate_parenthesis
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', The programs determines if the input string is valid parenthesis string.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1
Input: "()(){{}}[]" Output: True

Example 2
Input: "())){{}}[]" Output: False
"""

class Solver:
    def __init__(self):
        self.stack = []
        
    def reverseB(self,i):
        if i == "}":
            return "{"
        if i == "]":
            return "["
        if i == ")":
            return "("
        
    def insert(self,brace):
        if brace["type"] == "opening":
            self.stack = self.stack + [brace]
            return True
        else:
            if len(self.stack) == 0:
                return False
            else:
                if self.stack[-1]["string"] == self.reverseB(brace["string"]):
                    self.stack = self.stack[:-1]
                    return True
                else:
                    return False
    def build_dict(self,i):
        if i == "(" or i == "{" or i == "[":
            return {"type":"opening","string":i}
        if i == "]" or i == "}" or i == ")":
            return {"type":"closing","string":i}
        
    def is_empty(self,):
        return len(self.stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        sol = Solver()
        for i in s:
            solDict = sol.build_dict(i)
            res = sol.insert(solDict)
            if res == False:
                return False
        return sol.is_empty()
