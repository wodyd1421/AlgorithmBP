def solution(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if not(idx % 2):
                    ret += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != '1':
                if idx % 2:
                    ret += code[idx]
            else:
                mode = 0
    if ret == '':
        return 'EMPTY'
    return ret