# 큰 수의 법칙

# N == 배열의 크기, M == 숫자가 더해지는 횟수, K == 최대 중복 가능 개수
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

num1 = max(nums)
nums.remove(num1) # 가장 큰 수 중 가장 앞의 인덱스 꺼만 삭제함.
num2 = max(nums)

print((num1 * K + num2) * ( M // (K+1)) + num1 * (M % (K+1))) 
# 5 8 3
# 2 4 5 4 6 입력 시,
# (6 6 6 5) (6 6 6 5)