# 정수 내림차순으로 배치하기

def solution(n):
    answer = ''
    a = sorted(str(n), reverse = True)
    for i in range(len(a)):
        answer += a[i]
    return int(answer)

# .join(리스트)라는 리스트를 문자열로 합쳐주는 함수 존재. 
# return int("".join(ls)) 그래서 이렇게 풀기 가능.