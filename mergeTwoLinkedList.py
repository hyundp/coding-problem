# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 조건
# 1. 노드는 각각 50개까지 존재
# 2. 두 리스트 모두 오름차순

# 방법1
# 1. list1을 기준으로 list2의 노드들을 list1에 추가한다. time O(n), space O(1)
# 2. list1이 list2보다 클 때 list1의 current 전에 list2의 current node를 추가.
# 3. pre를 만들어서 list1이 이동하면 기존 list1을 pre로, list2가 이동하면 추가된 list2를 pre로 갱신해줌
# 4. 마지막으로 list1을 다 돌았는데 list2가 남아있다면 list2 나머지를 list1 뒤에 추가

def mergeTwoLists1(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not list1:
        return list2
    if not list2:
        return list1

    head = list1
    pre = None
    while list1 and list2:
        while list1.val >= list2.val:
            temp2 = list2.next
            list2.next = list1
            if pre:
                pre.next = list2
            if list1 == head:
                head = list2
            pre = list2
            list2 = temp2
            if not list2:
                break
        pre = list1
        list1 = list1.next
    if list2:
        pre.next = list2
    return head


# 방법2
# 1. 새로운 linked Node를 만들어서 두 리스트를 돌며 하나씩 추가하는 방법 time : O(n), space : O(1) -> 저장하는건 하나의 노드이기 때문


def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    temp = head = ListNode()
    
    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    
    if list1:
        temp.next = list1
    if list2:
        temp.next = list2


    return head.next