def solution(array, commands):
    answer = []
    for i in commands:
        tmp = array[i[0]-1:i[1]]
        sorted_tmp = sorted(tmp)
        answer.append(sorted_tmp[i[2]-1])
    return answer