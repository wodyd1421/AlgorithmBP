import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    ans=0
    c=hq.heappop(scoville)
    while c<K:
        hq.heappush(scoville,c)
        a=hq.heappop(scoville)
        try:
            b=hq.heappop(scoville)
        except:
            return -1
        hq.heappush(scoville,a+b*2)
        c=hq.heappop(scoville)
        ans+=1
    return ans