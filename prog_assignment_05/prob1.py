filename = 'dict_simplified.txt'
with open(filename, 'r') as f:
  lines = f.readlines()

arr = [line.strip() for line in lines]

words_dict = {}
for line in arr:
  if '\t' in line:
    word, meaning = line.split('\t', 1)
    words_dict[word.strip()] = meaning.strip()

vertex = list(words_dict.keys())

graph = {}

for word in vertex:
  graph[word] = {}    # 이웃 단어 -> 가중치

for i in range(len(vertex)):
  for j in range(i+1, len(vertex)):
    word_i = vertex[i]
    word_j = vertex[j]
    count_ij = words_dict[word_i].split().count(word_j)
    count_ji = words_dict[word_j].split().count(word_i)
    # 가중치(연관성)
    weight = count_ij + count_ji
    if weight > 0:
      graph[word_i][word_j] = weight
      graph[word_j][word_i] = weight


# 1번 문제: 정점, 엣지 개수
print(f"Answer1: {len(vertex)} {sum(len(neighbors) for neighbors in graph.values())//2}")

# 2번 문제: 최대 차수인 정점의 단어, 차수
max_degree = -1
max_word = None
for word, neighbors in graph.items():
  degree = len(neighbors)
  if degree > max_degree:
    max_degree = degree
    max_word = word
print(f"Answer2: {max_word} {max_degree}")

# 3번 문제: 가장 큰 연결 요소 크기
# DFS 써야 할 듯
visited = set()

def dfs(start):
  stack = [start]
  comp = []
  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      comp.append(node)
      stack.extend(graph[node].keys())
  return comp
  
max_connected_component = 0
for v in vertex:
  if v not in visited:
    component = dfs(v)
    if len(component) > max_connected_component:
      max_connected_component = len(component)
print(f"Answer3: {max_connected_component}")


# 4번 문제: 단어 x, 탐색 깊이 k -> x로부터 떨어진 거리가 k이하인 모든 단어 (x 맨 먼저 출력), 단어 개수
# BFS
from collections import deque

x=input().strip()
k=int(input().strip())

visited = set([x])
queue = deque([(x,0)])
result = [x]

while queue:
  current, dist = queue.popleft()
  if dist < k:
    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, dist+1))
        result.append(neighbor)

print("Answer4:")
for w in result:
  print(w)
print(len(result))

# 5번 문제: 임의 두 단어 연결하는 최단 경로의 길이, 경로에 등장하는 단어 순서대로 (경로 길이 = 엣지 가중치 역수의 합)
import heapq

start = input().strip()  # 출발 단어
end = input().strip()    # 도착 단어

dist = {v: float('inf') for v in vertex}
dist[start] = 0

prev = {v: None for v in vertex}

heap = [(0, start)]

while heap:
    cur_dist, cur_node = heapq.heappop(heap)
    if cur_dist > dist[cur_node]:
        continue
    if cur_node == end:
        break
    for neighbor, weight in graph[cur_node].items():
        cost = cur_dist + 1/weight
        if cost < dist[neighbor]:
            dist[neighbor] = cost
            prev[neighbor] = cur_node
            heapq.heappush(heap, (cost, neighbor))

if dist[end] == float('inf'):
    print("Answer5: no path")
else:
    path = []
    cur = end
    while cur:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    for i in range(len(path)):
      print(path[i], end='')
      if i != len(path)-1:
        print(" <==> ", end='')
    print(f"Distance: {dist[end]}")