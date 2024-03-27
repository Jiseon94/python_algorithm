import heapq

def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    # print(heap)
    
    heap.sort()
    # print(heap)
    
    cnt = 0
    
    while heap[0] < K :
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
        cnt +=1
        # print(heap)
        # print(cnt)
    
        if len(heap) == 1 and heap[0] < K:
            return -1
    return cnt
        
        
