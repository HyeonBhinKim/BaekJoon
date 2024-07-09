def solution(X, Y):
    answer = ''
    
    countx = [0]*10
    county = [0]*10
    
    for char in X:
        countx[int(char)] += 1
    for char in Y:
        county[int(char)] += 1
    
    for i in range(9, -1, -1):
        mincount = min(countx[i], county[i])
        
        if i == 0 and mincount > 0 and answer == '':
            return '0'
        
        elif mincount > 0:
            answer += str(i) * mincount
        
    if answer == '':
        return '-1'
    
    return answer