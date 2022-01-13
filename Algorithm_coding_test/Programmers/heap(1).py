# heapq 모듈 사용법
import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)


print(heap)

heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
        if scoville[0] >= K:
            return answer
        result_mix_scoville = heapq.heappop(
            scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, result_mix_scoville)
        answer += 1
