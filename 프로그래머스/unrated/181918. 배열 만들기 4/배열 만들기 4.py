def solution(arr):
    stk=[]
    i=0
    while i<len(arr):
        if stk==[]or stk[-1]<arr[i]:
            stk.append(arr[i])
            i+=1
        else:
            del stk[-1]
    return stk