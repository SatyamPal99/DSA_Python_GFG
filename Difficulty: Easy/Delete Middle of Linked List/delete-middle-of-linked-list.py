'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:

    def deleteMid(self, head):
        # Edge cases
        if not head or not head.next:
            return None

        # Step 1: count nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        # Step 2: find node BEFORE middle
        mid = count // 2
        temp = head

        for _ in range(mid - 1):
            temp = temp.next

        # Step 3: delete middle node
        temp.next = temp.next.next

        return head