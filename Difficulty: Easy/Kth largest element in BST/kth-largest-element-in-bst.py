# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        arr=[]
        q=deque([root])
        while q:
            temp=q.popleft()
            arr.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        arr.sort()
        n=len(arr)-k
        return arr[n]