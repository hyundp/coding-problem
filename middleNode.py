def middleNode1(self, head): # time: O(n), space : O(n)
    """
    :type head: ListNode
    :rtype: ListNode
    """
    size = 0
    result = ListNode()
    temp = head
    while(temp): # list의 크기를 구해서
        size+=1
        temp = temp.next
    mid = size//2 # 중간 인덱스를 찾고
    cnt = 0
    temp2 = head
    while(cnt<size): # 다시 listnode를 돌며
        if(cnt==mid): # 중간 인덱스가 나오면 그것을 head로 바꾼다.
            head = temp2 
            return head
        temp2 = temp2.next
        cnt+=1
    return head

def middleNode2(self, head): # time: O(n), space : O(n)
    arr = [head] # linked node를 array에 삽입 -> array의 0번째 index에 head가 들어간다는 의미
    while arr[-1].next: # array[index].next는 node.next와 같음. ex) array[0].next 는 head.next와 같음
        arr.append(arr[-1].next) # 각각의 head들을 array의 맨마지막에 추가함 -> array[0] == head, array[1] == head.next ...
    return arr[len(arr) // 2] # array라서 다시 loop하지 않아도 search가 한번에 가능.

def middleNode3(self, head): # time: O(n), space : O(1)
    slow = fast = head # 한칸씩 이동하는 slow랑 두칸씩 이동하는 fast를 만들면
    while fast and fast.next: # 2번 next가 진행되므로 fast와 fast.next의 null 체크를 모두 한다.
        slow = slow.next 
        fast = fast.next.next 
    return slow # fast가 끝나는 시점에 slow는 정확히 middle에 도착한다.