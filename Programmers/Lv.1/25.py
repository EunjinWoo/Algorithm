def solution(price, money, count):
    cnt = 0
    for i in range(1,count+1):
        cnt += i
    if (price*cnt - money) < 0:
        return 0
    else:
        return price*cnt - money
    
'''
다른 사람의 풀이

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
'''
