# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    cnt = 0
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
            cnt += 1
    if cnt == 0:
        answer.append(-1)
    return sorted(answer)

# 다른 풀이
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]