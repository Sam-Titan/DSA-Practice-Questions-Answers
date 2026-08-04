class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(5)
n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(7)

root.left = n1
root.right = n4
n1.left = n2
n1.right = n3

def print_all(node):
    if node is None:
        return
    
    print_all(node.left)
    print(node.val)
    print_all(node.right)

print_all(root)

def max_depth(node):
    if node is None:
        return 0

    count_left = max_depth(node.left)
    count_right = max_depth(node.right)

    return 1 + max(count_left, count_right)

result = max_depth(root)
print("The max depth of the tree:", result)