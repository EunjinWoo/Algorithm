a, b = map(int, input().strip().split(' '))

for row in range(b):
    for col in range(a):
        print("*", end="")
    print("")
    
"""
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b # 반복문 대신 곱하기 사용
print(answer)
"""
