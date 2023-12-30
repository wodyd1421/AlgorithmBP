def solution(my_string, m, c):
    answer = ''
    for n in range(len(my_string)//m):
        answer += my_string[m*n + c - 1]
    return answer