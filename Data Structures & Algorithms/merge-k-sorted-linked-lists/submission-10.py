# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None

        #Solution1:
        # return self.divide(lists)
    
        #Solution2 using min heaps
        minHeap=[]
        for i in range(len(lists)):
            lst=lists[i]
            heapq.heappush(minHeap,(lst.val,i,lst))
        
        res = ListNode()
        curr= res
        #test comment for sync test
        while len(minHeap)>0:
            val, index, popNode = heapq.heappop(minHeap)
            curr.next=popNode
            curr=curr.next
            if popNode.next:
                heapq.heappush(minHeap,(popNode.next.val,index,popNode.next))
        
        return res.next





    def divide(self, lists:List[Optional[ListNode]]):
        if len(lists)==1:
            return lists[0]
        start=0
        end=len(lists)-1
        mid=(start+end)//2

        # print(f"mid= {mid}")

        left = self.divide(lists[0:mid+1])
        right = self.divide(lists[mid+1:end+1])

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