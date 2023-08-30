# 하샤드 수

def solution(x):
    ha_num = sum(list(map(int, str(x))))
    if x % ha_num == 0:
        answer = True
    else:
        answer = False
    return answer