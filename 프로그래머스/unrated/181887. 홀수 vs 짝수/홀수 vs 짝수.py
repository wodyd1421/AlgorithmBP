def solution(num_list):
    o = sum(num_list[::2])
    e = sum(num_list[1::2])
    return max(o,e)