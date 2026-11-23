class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]
        for char in s :
            #if stacck is empty or character is different 
            if not stack or stack [-1][0]!=char:
                stack.append([char,1])
            else :
                #increase frequency of the same character 
                stack[-1][1]+=1
                #remove k consecutive characters 
                if stack[-1][1]==k:
                    stack.pop()
        #constructing the final string 
        res=""
        for char,count in stack :
            res+=count*char
        return res

