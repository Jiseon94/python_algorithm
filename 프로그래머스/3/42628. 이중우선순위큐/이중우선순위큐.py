import heapq

def solution(operations):
    answer = []
    # 조건 1 : 빈 배열에 삭제 연산은 무시. ==> 순서가 중요. 
    # 조건 2 : 같은 수일 때는 하나만 삭제.
    # 조건 3 : 문자열. 
    # 조건 4 : 최소 길이 1부터!
    heap = []
    for o in operations:
        if o.startswith("I"):
            num = o.split(" ")
            heapq.heappush(heap, int(num[1]))
        
        if o == "D 1":
            if len(heap) ==0:
                pass
            else:
                heap.sort()
                heap.reverse()
                # print(heap)
                heapq.heappop(heap)
        
        if o == "D -1":
            if len(heap) ==0:
                pass
            else:
                heapq.heapify(heap)
                heapq.heappop(heap)
               
    if len(heap) == 0:
        return [0,0]
    else:
        heap.sort()
        return [max(heap), min(heap)]