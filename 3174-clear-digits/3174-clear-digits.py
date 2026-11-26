class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        #creating a loop for traverse
        for char in s:
            #checking if char is digit 
            if char.isdigit():
                #only pop if stack is not empty 
                if stack:
                    stack.pop()
            #checking if the char is letter 
            else :
                stack.append(char)
        return "".join(stack)