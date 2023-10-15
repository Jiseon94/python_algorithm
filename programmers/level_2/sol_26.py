#경우의 수
#False : )로 시작. (로 끝.
# ( : 1
# ) : -1
# 인덱싱?


def solution(s):
    s.match('\(', 1, 1)
    print(s)

    answer = True

    return True

s = "(())()"
solution(s)

# 11 -1 -1 1 -1 = 0
# "(()("
# 0010
# ")()("
# -1 1 -1 1 =0
# "()()"
# 0101