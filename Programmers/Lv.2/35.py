def solution(s, n):
    answer = ''
    for char in s:
        if (ord(char)+n > 90 and ord(char) < 91) or (ord(char)+n > 122 and ord(char) < 123):
            answer += chr(ord(char)+n-26)
        elif char == " ":
            answer += " "
        else:
            answer += chr(ord(char)+n)
    return answer

"""
다른 사람의 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
"""
