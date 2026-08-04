class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(10)
n1 = TreeNode(6)
n2 = TreeNode(3)
n3 = TreeNode(8)
n4 = TreeNode(15)

root.left = n1
root.right = n4
n1.left = n2
n1.right = n3

print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)