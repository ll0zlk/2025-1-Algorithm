# PROG_ASSIGNMENT_01_2

# 입력: 정수 개수 N / 오름차순 정수 / K
# K랑 가까운 정수 (가까운 게 여러 개면 그 중 작은 거)

def binary_search(arr, k, begin, end):
  if begin > end:   # 교차된 상태!!!
    if end < 0:
      return arr[0]
    if begin >= len(arr):
      return arr[-1]
    
    if abs(arr[begin]-k) < abs(arr[end]-k):
      return arr[begin]
    else:   # end가 더 앞임
      return arr[end]

  mid = (begin+end)//2

  if arr[mid] == k:
    return arr[mid]
  elif arr[mid] > k:
    return binary_search(arr, k, begin, mid-1)
  else:   # arr[mid]<k
    return binary_search(arr, k, mid+1, end)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

nearest = binary_search(arr, k, 0, len(arr)-1)
print(nearest)