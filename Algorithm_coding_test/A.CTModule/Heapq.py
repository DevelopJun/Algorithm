# 힙 기능을 위한 표준 라이브러리
# 다익스트라 최단 경로 알고리즘 등 우선 순위 큐 기능을 구현할 때 사용한다.
# 코딩테스트 환경에서는 heapq 가 prioriyQueue 라이브러리보다 빠르게 작동한다.
import heapq
# heapq.heappush()  # 원소 삽입
# heapq.heappop()  # 원소 삭제


# 오름차순 정렬
# 파이썬에서는 최소 힙(Min Heap)이 구현되어 있기 때문에 원소를 힙에 전부 삽입 했다가 제거함으로써 오름차순으로 정렬 할 수 있다, O(NlogN)
def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, value)

    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result


result = heapsort([1, 9, 0, 7, 8, 6, 3, 5])
print(result)  # [0, 1, 3, 5, 6, 7, 8, 9]

# 내림차순 정렬
# 파이썬에서는 최대 힙(Max Heap) 이 구현되지 않기 떄문에 내림차순 정렬을 위해서는 부호를 바꾼 뒤 최소 힙을 이용하여
# 정렬하고 다시 부호를 바꿔주어야 한다.


def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, -value)
    print(heap)

    for i in range(len(heap)):
        result.append(-heapq.heappop(heap))
    return result


result = heapsort([1, 9, 0, 7, 8, 6, 3, 5])
print(result)
