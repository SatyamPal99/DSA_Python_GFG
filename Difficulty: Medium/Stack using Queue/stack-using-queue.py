from collections import deque


class myStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.appendleft(x)
        
            
            
        
    def pop(self):
        if len(self.q)==0:
            return
        self.q.popleft()
        
    def top(self):
        # return top element
        if len(self.q)==0:
            return -1
        return self.q[0]
        
    def size(self):
        return len(self.q)
        
