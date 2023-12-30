def solution(arr):
    ite = - 1
    arr_new = []
    while arr_new != arr:
        if arr_new != []:
            arr = arr_new
        arr_new = arr[:]
        for i in range(len(arr)):
            if arr[i] >= 50 and not arr[i] % 2:
                arr_new[i] = arr[i] / 2
            elif arr[i] < 50 and arr[i] % 2:
                arr_new[i] = 2 * arr[i] + 1
        ite += 1
    return ite