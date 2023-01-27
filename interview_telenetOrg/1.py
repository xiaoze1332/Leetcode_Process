def solution(a):

    stack = []
    a_set = set(a)

    res_list = []

    if len(a) == 1:
        return 1
    elif len(a) == 2:
        if a[0] == a[1]:
            return 1
        else:
            return 2
    elif len(set(a)) == 1:
        return 1
    else:
        for i in range(len(a)):
            if a[i] not in stack:
                stack.append(a[i])
            for j in range(i+1, len(a)):
                if a[j] not in stack:
                    stack.append(a[j])
                if len(stack) == len(a_set):
                    res_list.append(j-i+1)
                    stack = []
                    break
    
    return min(res_list)