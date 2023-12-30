def solution(todo_list, finished):
    a = []
    for i in range(len(todo_list)):
        a += [todo_list[i]] * int(not finished[i])
    return a