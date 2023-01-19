# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 조건
# 1. 별거없음

# 방법1 -> time : O(n), space : O(1)
# 1. 새로운 listNode를 만들어서 head를 갱신시킨다.
# 2. res 는 ListNode()로 만들면 마지막에 value 0이 남게되니 None부터 시작한다.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while(head):
            temp = head.next
            head.next = res
            res = head
            head = temp


        return res