#경우의 수
#False : )로 시작. (로 끝.
# ( : 1
# ) : -1
# 인덱싱?
import re


def solution(s):
    arr = []
    for i in range(len(s)):
        # print(s[i])
        #초반부터 걸러내기
        if s[0] == ')':
            return False
        if s[-1] == '(':
            return False
        #다음 조건
        if s[i] == '(':
            arr.append(1)
        else:
            arr.append(-1)
    print(arr)

    answer = True

    return True

s = "(())()"
print(solution(s))

# 11 -1 -1 1 -1 = 0
# "(()("
# 0010
# ")()("
# -1 1 -1 1 =0
# "()()"
# 0101