def solution(num_list):
    for c in num_list:
        if c < 0:
            return num_list.index(c)
    return -1