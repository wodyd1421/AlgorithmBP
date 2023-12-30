def solution(my_string, indices):
    my_string = list(my_string)
    d = 0
    for c in sorted(indices):
        del my_string[c - d]
        d += 1
    return ''.join(my_string)  