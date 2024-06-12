def solution(s, n):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    for char in s:
        if char in lower_alphabet:
            # 소문자인 경우
            index = lower_alphabet.index(char)
            shifted_index = (index + n) % 26
            result.append(lower_alphabet[shifted_index])
        elif char in upper_alphabet:
            # 대문자인 경우
            index = upper_alphabet.index(char)
            shifted_index = (index + n) % 26
            result.append(upper_alphabet[shifted_index])
        else:
            # 알파벳이 아닌 경우 (공백 등)
            result.append(char)

    return ''.join(result)