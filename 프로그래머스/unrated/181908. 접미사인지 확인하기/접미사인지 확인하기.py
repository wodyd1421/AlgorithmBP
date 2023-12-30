def solution(my_string, is_suffix):
    for e in range(len(my_string)):
        if is_suffix == my_string[e:]:
            return 1
    return 0