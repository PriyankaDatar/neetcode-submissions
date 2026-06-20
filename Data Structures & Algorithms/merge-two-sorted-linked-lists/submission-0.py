# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        new_list_head =None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
            
        if list1.val<list2.val:
            new_list = list1
            list1 = list1.next
            new_list_head = new_list
        elif list1.val==list2.val:
            new_list= list1
            list1=list1.next
            new_list_head = new_list
            new_list.next=list2
            list2=list2.next
            new_list= new_list.next
        else:
            new_list=list2
            list2=list2.next
            new_list_head = new_list



        while list1!=None and list2!=None:
            if list1.val<list2.val:
                new_list.next=list1
                new_list = new_list.next
                list1 = list1.next
            elif list1.val==list2.val:
                new_list.next=list1
                list1 = list1.next
                new_list = new_list.next
                new_list.next = list2
                new_list = new_list.next
                list2 = list2.next
            elif list1.val> list2.val:
                new_list.next =list2
                list2 = list2.next
                new_list = new_list.next
        
        if list2!=None:
            while list2!=None:
                new_list.next = list2
                list2 = list2.next
                new_list= new_list.next
        if list1!=None:
            while list1!=None:
                new_list.next = list1
                list1 = list1.next
                new_list= new_list.next
        
        return new_list_head
            
        