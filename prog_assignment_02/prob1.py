# 버블 정렬

import time
from heapq import *

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

def insertion_sort(arr):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[min_idx] > arr[j]:
        min_idx = j     # 여기까지 최솟값 찾기
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

def merge_sort(arr):
  n = len(arr)
  if n<2:
    return arr
  
  # 중간값 기준 분할
  mid = n // 2
  low = merge_sort(arr[:mid])
  high = merge_sort(arr[mid:])

  # 두 배열 돌면서 최솟값 찾기
  merged_arr = []
  l, h = 0, 0
  while l<len(low) and h<len(high):
    if low[l] < high[h]:
      merged_arr.append(low[l])
      l += 1
    else:
      merged_arr.append(high[h])
      h += 1
  
  merged_arr += low[l:]
  merged_arr += high[h:]
  return merged_arr

def quick_sort(arr):
  n = len(arr)
  if n <= 1:
    return arr
  
  pivot = arr[n//2]   # 피봇을 중간값으로 설정
  left = [i for i in arr if i < pivot]
  right = [i for i in arr if i > pivot]
  middle = [i for i in arr if i == pivot]
  return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
  heapify(arr)
  sorted_arr = []
  while arr:
    sorted_arr.append(heappop(arr))
  return sorted_arr

filename = "harry_full.txt"
with open(filename, 'r') as f:
  lines = f.readlines()

arr = [line.strip() for line in lines]

# 1) Bubble sort timing
arr1 = arr.copy()
t1 = time.time()
bubble_sort(arr1)
elasped1 = (time.time() - t1) * 1000

# 2) Insertion sort timing
arr2 = arr.copy()
t2 = time.time()
bubble_sort(arr2)
elasped2 = (time.time() - t2) * 1000

# 3) Merge sort timing
arr3 = arr.copy()
t3 = time.time()
merge_sort(arr3)
elasped3 = (time.time() - t3) * 1000

# 4) Quicksort timing
arr4 = arr.copy()
t4 = time.time()
quick_sort(arr4)
elasped4 = (time.time() - t4) * 1000

# 5) Heap sort timing
arr5 = arr.copy()
t5 = time.time()
heap_sort(arr5)
elasped5 = (time.time() - t5) * 1000

# 6) Library sort function timing
arr6 = arr.copy()
t6 = time.time()
sorted(arr6)
elasped6 = (time.time() - t6) * 1000

print(f"Bubble sort: {elasped1:.2f}ms")
print(f"Insertion sort: {elasped2:.2f}ms")
print(f"Merge sort: {elasped3:.2f}ms")
print(f"Quick sort: {elasped4:.2f}ms")
print(f"Heap sort: {elasped5:.2f}ms")
print(f"Library sort function: {elasped6:.2f}ms")