import sys
sys.setrecursionlimit(10**6)

def is_postorder(postorder, start, end):
    if start >= end:
        return True

    root = postorder[end]
    i = start
    while i < end and postorder[i] < root:
        i += 1
    mid = i
    while i < end:
        if postorder[i] < root:
            return False
        i += 1
    return is_postorder(postorder, start, mid - 1) and is_postorder(postorder, mid, end - 1)

# 트리 노드 클래스
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

# 트리 높이 계산
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

# 메인
n = int(input())
arr = list(map(int, input().split()))

if len(arr) != n:
    print(-1)
elif not is_postorder(arr, 0, n - 1):
    print(-1)
else:
    root = bst(arr, 0, n - 1)
    print(height(root))
