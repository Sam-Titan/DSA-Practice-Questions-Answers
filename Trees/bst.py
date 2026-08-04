class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)

    return root

val = [15, 10, 20, 8, 12, 17, 25]

root = None
for i in val:
    root = insert_bst(root, i)

def inorder(root):
    result = []
    def function(root):
        if root is None:
                return
        function(root.left)
        result.append(root.val)
        function(root.right)
    function(root)
    return result

res = inorder(root)
print("The Inorder format:", res)

def search_bst(root, val):
    if root is None:
        return None
    
    if val == root.val:
        return root
    elif val < root.val:
        print(root.val)
        return search_bst(root.left, val)
    else:
        print(root.val)
        return search_bst(root.right, val)

p = 8
q = 12
def LCA(root, p, q):
    if root is None:
        return None

    if p < root.val and q < root.val:
        return LCA(root.left, p, q)
    elif p > root.val and q > root.val:
        return LCA(root.right, p, q)
    else:
        return root.val

result = LCA(root, p, q)

print("The LCA is:", result)

result = search_bst(root, 13)
print("The Search gave:", result)