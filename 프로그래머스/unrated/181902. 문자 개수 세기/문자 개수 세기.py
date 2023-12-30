def solution(my_string):
    dic = {}
    for m in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        dic[m] = my_string.count(m)
    return list(dict(sorted(dic.items())).values())