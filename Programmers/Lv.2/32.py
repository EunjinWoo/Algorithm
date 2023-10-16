def solution(number):
    cnt = 0
    for a in range(len(number)):
        num1 = number[a]
        for b in range(a+1, len(number)):
            num2 = number[b]
            for c in range(b+1, len(number)):
                num3 = number[c]
                if num1+num2+num3 == 0:
                    cnt += 1
    return cnt
