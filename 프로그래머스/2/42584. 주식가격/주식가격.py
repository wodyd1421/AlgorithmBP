def solution(prices):
    ans=[]
    for i in range(len(prices)):
        sec=0
        for j in range(i,len(prices)-1):
            if prices[i]<=prices[j]:
                sec+=1
            else:
                break
        ans.append(sec)
    return ans