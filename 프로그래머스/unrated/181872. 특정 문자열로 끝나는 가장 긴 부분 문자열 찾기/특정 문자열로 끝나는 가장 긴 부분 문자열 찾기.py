def solution(myString, pat):
    for i in range(len(myString)):
        if myString[-i-1] == pat[-1]:
            for j in range(len(pat)-1):
                if pat[-j-2] != myString[-i-j-2]:
                    break
            return myString[:len(myString)-i]