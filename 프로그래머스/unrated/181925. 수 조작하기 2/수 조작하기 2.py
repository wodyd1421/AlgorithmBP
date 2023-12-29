def solution(numLog):
    answer = ''
    key = dict(zip([1,-1,10,-10],['w','s','d','a']))
    for c in range(len(numLog)-1):
        answer += key[numLog[c+1]-numLog[c]] 
    return answer