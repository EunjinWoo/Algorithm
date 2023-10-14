def solution(arr1, arr2):
    answer = []
    for row in range(len(arr1)):
        answer.append([])
        for col in range(len(arr1[0])):
            answer[row].append(arr1[row][col] + arr2[row][col])
    return answer

# 다른 사람의 풀이
# def sumMatrix(A,B):
#    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
#    return answer
