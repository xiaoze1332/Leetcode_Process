# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        node_index_dict = {}

        while head != None:
            if head in node_index_dict:
                return head
            else:
                node_index_dict[head] = 1
                head = head.next

        return None