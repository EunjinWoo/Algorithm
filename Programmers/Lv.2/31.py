def solution(s):
    answer = ''
    cnt = 0
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            cnt=0
        else:
            if (cnt%2 == 0):
                answer += s[i].upper()
                cnt += 1
            else:
                answer += s[i].lower()
                cnt += 1
    return answer

"""
def solution(s):
    answer = ''
    words = s.split(" ") -> 이것도 split()이랑 split(" ") 이랑 점수가 달랐음. split()으로 하면 여러개의 공백일 때 하나로 합쳐진다고..
    for word in words:
        for i in range(0,len(word)):
            if (i%2 == 0):
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "
    return answer.strip() 
-> 이렇게 하니 아마 문장 앞 뒤에 공백이 있는 경우 그게 그대로 반영되지 않아서 문제가 생긴 듯.
"""
"""
def solution(s):
    answer = ''
    words = s.split(" ")
    for word in words:
        word = word.lower()
        for i in range(0,len(word)):
            if (i%2 == 0):
            a = word[i].upper()
            word = word[:i] + a + word[i+1:] -> word[1:] 이게 존재하지 않는 그냥 문자 하나짜리도 있어서 문제였던 건거 같음.
        answer += " "
    return answer.strip()
"""
"""
다른 사람의 풀이 :
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
"""
