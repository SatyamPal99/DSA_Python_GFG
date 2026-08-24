from collections import deque
import math
class Solution:
    def minSteps(self, arr, start, end):
        if start == end:
            return 0
        q=deque()
        dist=[math.inf]*9999
        q.append((0,start)) # steps, node
        dist[start]=0
        while q:
            steps,node=q.popleft()
            for i in arr:
                num=(node*i)% 1000 
                if steps+1<dist[num]:
                    dist[num]=steps+1
                    q.append((steps+1,num))
                    if num==end:
                        return steps+1
        return -1
                    