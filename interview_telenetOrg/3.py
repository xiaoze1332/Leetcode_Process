def solution(a):
  # Write your answer

    res = []

    for i, char in enumerate(a):
        if char.isdigit():
            tmp = int(char)
            res.append(tmp)
        elif  (char.startswith('-') and char[1:] or char).isdigit():
            tmp = int(char)
            res.append(tmp)
        elif char == 'C':
            res.pop()
        elif char == 'D':
            res.append(res[-1]*2)
        elif char == '+':
            res.append(res[-1] + res[-2])

    return sum(res)