# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = result = ListNode(0, None)
        carry = 0

        while l1 or l2 or carry:
            v1 = 0
            v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next    
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            sum = v1 + v2 + carry
            carry = sum // 10
            sum %= 10

            curr_node.next = ListNode(sum, None)
            curr_node = curr_node.next
        return result.next



        