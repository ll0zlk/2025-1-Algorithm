class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 후위 순서로 BST 구성
def bst(postorder, start, end):
    if start > end:
        return None
    root_val = postorder[end]
    root = Node(root_val)
    i = start
    while i < end and postorder[i] < root_val:
        i += 1
    root.left = bst(postorder, start, i - 1)
    root.right = bst(postorder, i, end - 1)
    return root

def preorder(node):
  if node:
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)

n = int(input())
arr = list(map(int, input().split()))

preorder(bst(arr, 0, n-1))