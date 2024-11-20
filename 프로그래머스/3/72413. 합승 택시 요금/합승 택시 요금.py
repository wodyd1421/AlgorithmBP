def solution(n, s, a, b, fares):
    floyd = [[100000*(n-1)]*(n+1) for _ in range(n+1)]
    
    for edge in fares:
        floyd[edge[0]][edge[1]]=floyd[edge[1]][edge[0]]=edge[2]
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j:
                    floyd[i][j]=0
                    continue
                floyd[i][j]=min(floyd[i][k]+floyd[k][j],floyd[i][j])
                
    answer=floyd[s][a]+floyd[s][b]
    
    for i in range(1,n+1):
        answer=min(answer,floyd[s][i]+floyd[i][a]+floyd[i][b])
    return answer