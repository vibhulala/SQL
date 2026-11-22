class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        invalid=set()
        #first traversal 
        for i , char in enumerate(s):
            if char =='(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    invalid.add(i)
        #remaining opening brackets are invalid 
        while stack:
            invalid.add(stack.pop())
        #constructing the final valid string 
        res=[]
        for i , char in enumerate (s):
            if i not in invalid :
                res.append(char)
        return "".join(res)