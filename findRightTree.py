"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root): # time : O(n), space : O(n)
        """
        :type root: Node
        :rtype: Node
        """
        # 조건
        # 1. 모든 레벨 노드가 다 가득 차 있는 퍼펙트 이진트리다.
        # 2. next는 오른쪽에 있는 node를 뜻한다. -> 처음에는 모든 next pointer가 null이다.
        # 3. 노드 개수는 [0, 2^12-1], 노드값은 -1000 ~ 1000 사이 존재

        # 의문
        # 1. 단순 숫자계산 방식 말고, 레벨이 바뀐다는 것을 어떻게 알 수 있을까? -> 2중으로 나누어서 레벨별로 다룰 수 있게 만든다.

        # 방법
        # 1. right를 지정해서 오른쪽부터 bfs를 진행하게 한다. 이때 레벨이 바뀌면 right는 None로 되니 가장 오른쪽 노드들은 모두 next가 None이 될 수 있다.

        queue = [root]
        if not root:
            return root
        while len(queue):
            right = None
            s = len(queue)
            for _ in range(s):
                t = queue.pop(0)
                t.next, right = right, t
                if t.right:
                    queue.extend([t.right, t.left]) # extend는 껴넣기, append는 옆에 넣기
        return root
    
    def connect(self, root): # time : O(n), space : O(1) -> 자료구조로 저장할 필요없이 그냥 값만 쓰면 됨
        """
        :type root: Node
        :rtype: Node
        """
        # 방법
        # 2. 부모 레벨에서 자식 레벨들에 대한 next를 처리해줌. 마찬가지로 level별로 나누기 위해 while문을 2개 사용.

        temp_root = root
        while(temp_root):
            temp_root, current = temp_root.left, temp_root
            while(current):
                if current.left: # 레벨 처리. current가 next가 존재한다면 자식들을 모두 연결해줘야하므로 조건 추가
                    current.left.next = current.right
                    if current.next:
                        current.right.next = current.next.left
                else:
                    break
                current = current.next
        return root