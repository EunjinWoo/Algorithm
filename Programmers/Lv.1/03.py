# 자릿수 더하기

def solution(n):
    answer = 0
    
    while n != 0:
        answer += n%10
        n = (n-(n%10)) // 10

    return answer