# PROG_ASSIGNMENT_01_1

# 입력: 정수 개수 N / 정수 / K
# K의 rank == K보다 작은 것 개수 + 1
## 오름차순 정렬했을 때 위치!!
# 반복문 사용 금지
# O(N) 이하

def recursion(arr, k, index=0):
  if index == len(arr):
    return 0
  return (arr[index] < k) + recursion(arr, k, index + 1)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

rank = recursion(arr, k) + 1
print(rank)