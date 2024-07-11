def solution(s):
    answer = 0
    sav1=0
    sav2=0

    for i in s:
        # 시작시 추가하면 마무리를 체크하지 않고 끝나도 값이 같다.
        if sav1==sav2:
            answer+=1
            a=i
            
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer