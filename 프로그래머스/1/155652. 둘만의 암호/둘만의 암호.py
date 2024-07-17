def solution(s, skip, index):
    
    alphabet = []
    answer = []
    
    for i in range(97, 123):
        if chr(i) not in skip:
            alphabet.append(chr(i))
    
    for spel in s:
        tmp = alphabet.index(spel)
        new_spel = alphabet[(tmp+index)%len(alphabet)]
        answer.append(new_spel)
    
    return ''.join(answer)
    