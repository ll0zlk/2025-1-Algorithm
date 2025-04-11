# PROG_ASSIGNMENT_02_3

# 새 원소 맨 끝에
# 최대값 삭제 후 맨 마지막 원소를 그 위치로
# 이렇게 된 우선순위큐 vs 힙으로 우선순위큐

# 정수 N개 랜덤 생성 -> 우선순위큐 삽입
# M번 삽입/삭제 연속 실행에 걸리는 총 시간 측정
# M번 연산 = 1/2 확률로 삽입/삭제 결정 -> 삽입이면 반복

import random
import time
import heapq

class ArrayPQ:
  def __init__(self):
    self.data = []

  def add(self, value):
    self.data.append(value)
  
  def extractMax(self):
    if not self.data:
      return None
    max_index = 0
    # 최대값 인덱스 찾기
    for i in range(1, len(self.data)):
      if self.data[i] > self.data[max_index]:
        max_index = i
    max_value = self.data[max_index]  # 최대값
    self.data[max_index] = self.data[-1]  # 최대값 자리에 맨 마지막 원소로 대체
    self.data.pop() # 맨 마지막 중복되니까 삭제
    return max_value
  
  def empty(self):
    return len(self.data) == 0
  
class HeapPQ:
  def __init__(self):
    self.data = []

  def add(self, value):
    heapq.heappush(self.data, -value)

  def extractMax(self):
    if not self.data:
      return None
    return -heapq.heappop(self.data)
  
  def empty(self):
    return len(self.data) == 0
  
def test(pqueue_class, N, M):
  pqueue = pqueue_class()
  rd = random.Random(42)

  for _ in range(N):
    pqueue.add(rd.randint(0, N))

  start = time.time()
  for _ in range(M):
    if rd.randint(0,1) == 0 or pqueue.empty():
      pqueue.add(rd.randint(0,N))
    else:
      pqueue.extractMax()
  end = time.time()

  return end-start

N, M = 100000, 100000
print(f"정렬되지 않은 배열: {test(ArrayPQ, N, M)}")
print(f"우선순위 큐: {test(HeapPQ, N, M)}")