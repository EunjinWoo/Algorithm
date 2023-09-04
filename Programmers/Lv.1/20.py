# 가운데 글자 가져오기

def solution(s):
    answer = ''
    if len(s)%2 == 0:
        answer = s[((len(s)-1) // 2):((len(s)-1) // 2) + 2]
    else:
        answer = s[((len(s)-1) // 2)]
    return answer

# 다른 사람의 풀이
# def solution(s):
#     return s[(len(s)-1)//2 : len(s)//2 + 1]