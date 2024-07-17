def solution(s, skip, index):
    # 알파벳 리스트에서 skip에 포함된 문자를 제외
    alphabets = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    # 변환된 결과를 저장할 리스트
    result = []
    
    for char in s:
        # 현재 문자의 위치를 찾음
        current_pos = alphabets.index(char)
        # index만큼 뒤의 위치를 계산
        new_pos = (current_pos + index) % len(alphabets)
        # 변환된 문자를 결과에 추가
        result.append(alphabets[new_pos])
    
    # 리스트를 문자열로 변환하여 반환
    return ''.join(result)