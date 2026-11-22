class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for digit in num :
            while  stack and k> 0 and stack [-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        #remove remaining digits from the end 
        if k>0:
            stack=stack[:-k]
        #remove leading zeroes
        result="".join(stack).lstrip("0")
        return result if result else "0"