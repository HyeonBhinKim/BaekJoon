def solution(lottos, win_nums):
    answer = []
    passcount = lottos.count(0)
    wincount = len(set(lottos) & set(win_nums))
    
    def getrank(n):
        if n == 6:
            return 1
        elif n == 5:
            return 2
        elif n == 4:
            return 3
        elif n == 3:
            return 4
        elif n == 2:
            return 5
        else:
            return 6
    
    
    
    return [getrank(passcount+wincount),getrank(wincount)]