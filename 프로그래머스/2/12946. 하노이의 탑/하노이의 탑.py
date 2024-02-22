answer = []
def solution(n, start=1, end=3):
    if n == 1:
        answer.append([start, end])
        return answer
    mid = 6 - start - end
    solution(n-1, start, mid)
    answer.append([start, end])
    solution(n-1, mid, end)
    return answer