def solution(arr, flag):
    X = []
    for i, j in enumerate(flag):
        if j:
            X += [arr[i]]*arr[i]*2
        else:
            for k in range(arr[i]):
                del X[-1]
    return X