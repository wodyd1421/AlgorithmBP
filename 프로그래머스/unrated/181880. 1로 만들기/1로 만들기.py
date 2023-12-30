def solution(num_list):
    op_cnt = 0
    for c in num_list:
        while c != 1:
            if not c % 2:
                c /= 2
            else:
                c = (c - 1) / 2
            op_cnt += 1
    return op_cnt