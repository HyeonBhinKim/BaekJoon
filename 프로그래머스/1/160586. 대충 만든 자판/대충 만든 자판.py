def solution(keymap, targets):
    answer = []
    number = {}
    for i in keymap:
        for index, ini in enumerate(i):
            if ini in number:
                number[ini] = min(index+1, number[ini])
            else:
                number[ini] = index + 1
    
    for ans in targets:
        tmp = 0
        for x in ans:
            if x in number:
                tmp += number[x]
            else:
                tmp = -1
                break
        answer.append(tmp)
    
    return answer