def solution(n):
    ans = [[0]*n for i in range(n)]
    if n%2:
        for i in range(-(-n//2)):
            k = -(-n//2)-1-i
            l = n**2-8*k*(k+1)//2
            if k == 0:
                ans[i][i] = n**2
            for j in range(4*((n-2*i)-1)):
                if j < (n-2*i)-1:
                    ans[i][i+j] = l+j
                elif j < ((n-2*i)-1)*2:
                    ans[i+j-((n-2*i)-1)][(n-1)-i] = l+j
                elif j < ((n-2*i)-1)*3:
                    ans[(n-1)-i][n-1-(i+j-((n-2*i)-1)*2)] = l+j
                else:
                    ans[n-1-(i+j-((n-2*i)-1)*3)][i] = l+j
    else:
        for i in range(-(-n//2)):
            k = -(-n//2)-1-i
            l = n**2+1-4*(n//2-i)**2
            if k == 0:
                ans[i][i] = n**2
            for j in range(4*((n-2*i)-1)):
                if j < (n-2*i)-1:
                    ans[i][i+j] = l+j
                elif j < ((n-2*i)-1)*2:
                    ans[i+j-((n-2*i)-1)][(n-1)-i] = l+j
                elif j < ((n-2*i)-1)*3:
                    ans[(n-1)-i][n-1-(i+j-((n-2*i)-1)*2)] = l+j
                else:
                    ans[n-1-(i+j-((n-2*i)-1)*3)][i] = l+j
    return ans