answer = []
def solution(n, start=1, end=3):
    if n == 1:
        answer.append([start, end])
        return answer
    if start + end == 4:
        mid = 2
    elif start + end == 3:
        mid = 3
    else:
        mid = 1
    solution(n-1, start, mid)
    answer.append([start, end])
    solution(n-1, mid, end)
    return answer