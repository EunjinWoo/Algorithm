def solution(sizes):
    width = max(map(max, sizes)) # 전체 2차원 배열에서 가장 큰 값 찾기
    a = []
    for i in range(len(sizes)):
        a.append(min((sizes[i])))
    height = max(a)
    return width*height

"""
# 다른 사람의 풀이. 개념은 같음. 이게 훨씬 좋은 코드

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
"""
