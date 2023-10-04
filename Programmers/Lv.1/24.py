def solution(s):
    answer = ''
    a = []
    for i in s:
        a.append(i)
    a.sort(reverse=True)
    for i in a:
        answer += i
    return answer

'''
다른 사람의 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))

'''
