# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head=head
        prev = None 
        
        while head :
            tmp = head
            new_head = head.next
            head.next = prev
            prev = head
            head = new_head
            # print(prev.val)            

        return prev


        