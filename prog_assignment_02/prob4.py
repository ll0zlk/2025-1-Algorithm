# convex_hull
# 분할정복법

def cross(o, a, b):
  return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def convex_hull(points):
  points = sorted(set(points))

  if len(points) <= 1:
    return points
  
  lower = []
  for p in points:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
      lower.pop()
    lower.append(p)

  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
      upper.pop()
    upper.append(p)

  return lower[:-1] + upper[:-1]

filename = "input4.txt"
with open(filename, 'r') as f:
  lines = f.readlines()

points = [tuple(map(int, line.strip().split())) for line in lines[1:]]

hull = convex_hull(points)

for x, y in hull:
  print(x, y)