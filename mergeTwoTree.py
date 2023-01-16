# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2): # time : O(n), space : O(n)
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        # 1. root부터 시작해서 왼쪽 자식을 먼저 돈다.
        # 2. 트리의 끝인지 어떻게 확인하지? -> left와 right가 모두 없으면 그 노드는 끝난 것.
        stack = []
        stack.append((root1, root2))
        while(len(stack)): # 하나의 트리에 집중하는 이 방식은 모든 node를 다 돌 수 있다고 어떻게 장담하는지? -> 다른 트리에 있는 것까지 나한테 다 넘겨줘서 처리하기 때문에 모든 node가 처리된다.
            t = stack.pop()
            if t[0] == None or t[1] == None: # 부모 노드에서 처리가 된 경우 or 처리하지 않고 놔둬도 되는 경우
                continue
            t[0].val += t[1].val
            if t[0].left == None:
                t[0].left = t[1].left # t[0]을 기준으로 보고 있기 때문에 만약 t[1]이 없는 경우라면 그냥 넘어가면 되지만 t[0]이 없는 경우라면 t[1]에 있는걸 불러와야한다. 값만이 아니라 노드 전체(그 노드의 자식들까지)를 가져와서 이후의 계산에서 t[1]의 자식들도 계산되게 만드는 것이다.
            else:
                stack.append((t[0].left, t[1].left))
            
            if t[0].right == None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return root1