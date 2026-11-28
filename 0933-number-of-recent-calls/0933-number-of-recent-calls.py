from collections import deque 
class RecentCounter:

    def __init__(self):
        self.q=deque()
    def ping(self, t: int) -> int:
        #adding the correct timestamp 
        self.q.append(t)
        #removing the outdated timestamps
        while self.q and self.q[0]<t-3000:
            self.q.popleft()
        #rturning number of valid parentheses
        return len (self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)