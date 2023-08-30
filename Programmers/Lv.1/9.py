# 정수 제곱근 판별
import math

def solution(n):
    answer = 0
    if int(math.sqrt(n)) == math.sqrt(n):
        answer = (math.sqrt(n) + 1) ** 2
    else:
        answer = -1
    return answer

# math module import 하지 말고 sqrt면 그냥 **(1/2)로 쓰기