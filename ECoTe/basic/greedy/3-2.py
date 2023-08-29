# 큰 수의 법칙

# N == 배열의 크기, M == 숫자가 더해지는 횟수, K == 최대 중복 가능 개수
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

num1 = max(nums) # 가장 큰 수
nums.remove(num1) # 가장 큰 수 중 가장 앞의 인덱스 꺼만 삭제함.
num2 = max(nums) # 두 번째로 큰 수 (num1과 같을 수 있음)

print((num1 * K + num2) * ( M // (K+1)) + num1 * (M % (K+1))) 
# 5 8 3
# 2 4 5 4 6 입력 시,
# (6 6 6 5) (6 6 6 5)

# ---- 1,2 번째로 큰 수 뽑는 부분만 다름. 개념은 잘 풀었다. ----
# nums.sort() # 입력받은 수 정렬
# num1 = nums[n-1]
# num2 = nums[n-2]
# 이렇게 함.