class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        #vriable to navigate to through length of target len(target)
        l=0
        #array of stack oeprations 
        res=[]
        for i in range(1,n+1):
            if l>=len(target):
                break
            res.append("Push")
            if i!=target[l]:
                res.append("Pop")
            else:
                l+=1
        return res