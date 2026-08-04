from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)

root.left = n1
root.right = n2
n2.left = n3
n2.right = n4

result = []
def inorder_traversal(root):
    if not root:
        return 0
    
    inorder_traversal(root.left)
    result.append(root.val)
    inorder_traversal(root.right)

inorder_traversal(root)
print(result)

def levelOrder(root):
    if not root:
        return []
    
    q = deque([root])
    result = []
    while q:
        level_length = len(q)
        level = []
        for _ in range(level_length):
            current = q.popleft()
            level.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        result.append(level)
    return result

res = levelOrder(root)
print(res)
