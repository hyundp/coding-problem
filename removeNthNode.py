def removeNthFromEnd1(self, head, n): # time : O(n), space : O(n)
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # 없어져야 하는 포인트를 찾고 정방향으로 진행 후 연결을 바꾼다.
    size = 0
    temp1 = temp2 = head
    while(temp1):
        temp1 = temp1.next
        size+=1
    index = size-n
    if(index<=0): # 같다면 첫번째 제거, 조건에서 n이 사이즈보다 같거나 작으므로 음수는 될 수 없긴함.
        return head.next # 이걸로 밑의 경우의 예외를 모두 제거했다는 확신이 필요함.
    cnt = 1
    while(cnt < index):
        temp2 = temp2.next
        cnt+=1
    temp2.next = temp2.next.next
    return head


def removeNthFromEnd2(self, head, n): # use two pointer -> 양 끝에서 내려가는 방식이 아니라 같은 방향 다른 출발선을 활용
    fast, slow = head, head
    for _ in range(n): # fast먼저 n만큼 보내고
        fast = fast.next
    if not fast: # 첫번째 제거는 더 pre가 없기 때문에 따로 처리해준다.
        return head.next
    while fast.next: # fast를 끝까지 보내면 자연스럽게 slow는 제거해야할 노드의 전 노드가 된다. (fast는 한칸 더 간 셈이기 때문에.)
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next # 첫번째 노드가 아니면 제거 노드의 그 전 노드를 찾는 것이므로 무조건 next.next가 null이라도 존재하게 된다.
    return head