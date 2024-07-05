def solution(babbling):
    answer = 0
    cansay = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        tmp = ''
        said = ''
        for j in i:
            tmp += j
            if tmp in cansay and tmp != said:
                said = tmp
                tmp = ''
            if len(tmp) > 3:
                break
        if tmp == '':
            answer +=1
        
    return answer