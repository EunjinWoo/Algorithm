# 없는 숫자 더하기

def solution(numbers):
    nums = [0,1,2,3,4,5,6,7,8,9]
    for num in numbers:
        nums.remove(num)
    return sum(nums)

# 다른 사람 풀이
# def solution(numbers):
#     return 45 - sum(numbers)