def solution(n):
    a = ''
    answer = 0
    while n>0:
        n, mod = divmod(n, 3) # n을 3으로 나눈 몫이 다시 n에, 나머지가 mod에 들어감.
        a += str(mod) # 이렇게 나온 a가 앞뒤반전된 3진법
    a = a[::-1] # 이걸 다시 제대로 된 3진법으로 돌려서 앞에부터 차례대로 1,3,9 .. 곱해서 더하기
    for i in range(len(a)):
        answer += int(a[i])*(3**i)
    return answer
