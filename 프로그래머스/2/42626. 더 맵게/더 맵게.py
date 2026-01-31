import heapq
def solution(scoville, K):
    summ = 0
    # scoville.sort()
    heapq.heapify(scoville)
    while scoville:
        a = heapq.heappop(scoville)
        #아직 부족함
        if a < K: 
            if scoville:
                b = heapq.heappop(scoville)
                heapq.heappush(scoville, (a + b * 2))
                summ += 1
            else: 
                return -1
        else: 
            return summ
        
    return -1