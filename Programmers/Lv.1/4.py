# 약수의 합

def solution(n):
    answer = 0
    for i in range(1,n+1): # division by zero error 주의.
        if n%i == 0:
            answer += i
    return answer