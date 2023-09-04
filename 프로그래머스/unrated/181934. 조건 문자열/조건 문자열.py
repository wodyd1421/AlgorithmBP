def solution(ineq, eq, n, m):
    if eq == "!":
        eq = ''
    if eval(str(n) + ineq + eq + str(m)):
        return 1
    else:
        return 0