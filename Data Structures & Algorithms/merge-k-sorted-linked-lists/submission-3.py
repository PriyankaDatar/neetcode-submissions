# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None


        return self.divide(lists)
    
    def divide(self, lists:List[Optional[ListNode]]):
        if len(lists)==1:
            return lists[0]
        start=0
        end=len(lists)-1
        mid=(start+end)//2

        # print(f"mid= {mid}")

        left = self.mergeKLists(lists[0:mid+1])
        right = self.mergeKLists(lists[mid+1:end+1])

        mergedList = self.merge(left, right) 
        return mergedList       

    # same code as merge two sorted lists
    def merge(self, l1:ListNode, l2: ListNode)-> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next