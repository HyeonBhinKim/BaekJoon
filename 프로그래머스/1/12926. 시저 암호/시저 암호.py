def solution(s, n):
    result = []
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in s:
        if char in lower:
            num = lower.index(char)
            shift = lower[(num+n)%26]
            result.append(shift)
        elif char in upper:
            num = upper.index(char)
            shift = upper[(num+n)%26]
            result.append(shift)
        else:
            # 알파벳이 아닌 경우 (공백 등)
            result.append(char)

    return ''.join(result)