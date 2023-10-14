def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)

# 다른 사람의 풀이
#  return s.isdigit() and len(s) in [4,6]
