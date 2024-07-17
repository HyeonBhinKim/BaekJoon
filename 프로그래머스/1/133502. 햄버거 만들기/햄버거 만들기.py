def solution(ingredient):
    
    tmp = []
    answer = 0
    
    for i in ingredient:
        tmp.append(i)
        if tmp[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                tmp.pop()
        
#         tmp.append(i) # stack 시간복잡도 O(1)
#         if len(tmp) >= 4 and tmp[-4:] == [1,2,3,1]:
#             del tmp[-4:]
#             answer += 1
    
    # for i in ingredient:
    #     tmp += str(i)  시간복잡도 O(n)
    #     if '1231' in tmp:  시간복잡도 O(n) => O(n^2)
    #         answer += 1
    #         tmp = tmp.replace('1231','')  시간복잡도 O(n)
        
    return answer