# PROG_ASSIGNMENT_03_1

class Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def preorder(node):
  if node:
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
  if node:
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=' ')

filename = 'input1.txt'
with open(filename, 'r') as f:
  lines = f.readlines()

n = int(lines[0])
node_info = [list(map(int, line.strip().split())) for line in lines[1:]]

nodes = {}
for val, _, _ in node_info:
  nodes[val] = Tree(val)  # 노드 값 채우기기

has_parent = {val: False for val in nodes} # 부모 여부 확인

for i in range(n):
  val, left, right = node_info[i]
  if left != -1:  # 왼쪽 자식이 있으면
    nodes[val].left = nodes[left]   # 왼쪽 자식에 해당 노드 연결
    has_parent[left] = True   # 해당 노드는 부모 있음
  if right != -1:
    nodes[val].right = nodes[right]
    has_parent[right] = True

root_val = next(val for val, has in has_parent.items() if not has)
root = nodes[root_val]

preorder(root)
print()
inorder(root)
print()
postorder(root)