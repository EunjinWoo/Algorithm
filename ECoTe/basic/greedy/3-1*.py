# 거스름돈

N = int(input())
cnt = 0

while N != 0:
    if N >= 500:
        cnt += N//500
        N = N % 500
    elif N >= 100:
        cnt += N // 100
        N = N % 100
    elif N >= 50:
        cnt += N // 50
        N = N % 50
    elif N >= 10:
        cnt += N // 10
        N = N % 10

print(f"거슬러 줘야 할 동전의 최소 개수는 {cnt}개 입니다.")

# 더 나은 코드 :
N = int(input())
cnt = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    cnt += N // coin
    N = N % coin

print(f"거슬러 줘야 할 동전의 최소 개수는 {cnt}개 입니다.")