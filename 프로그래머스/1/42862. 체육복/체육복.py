def solution(n, lost, reserve):
    # 여벌 체육복을 가진 학생 중에서 도난당한 학생을 먼저 처리
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    
    answer = n - len(new_lost)
    
    for i in new_lost:
        if i-1 in new_reserve:
            answer += 1
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            answer+= 1
            new_reserve.remove(i+1)
            
    return answer