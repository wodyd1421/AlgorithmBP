def solution(n):
    answer = 0
    if n % 2:
        for m in range(1, n + 1):
            if m % 2:
                answer += m
    else:
        for m in range(1, n + 1):
            if not(m % 2):
                answer += m * m
    return answer