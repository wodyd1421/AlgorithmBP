def solution(s):
    answer = []
    for i in range(len(s)):
        for j in range(1, i+1):
            if s[i-j] == s[i]:
                answer.append(j)
                break
        if len(answer) != i+1:
            answer.append(-1)
    return answer