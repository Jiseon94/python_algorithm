# 1. 디폴트는 True
# 2. P,p와 Y,y의 개수 체크. 다르면 False 주는 조건만 추가.
# 3. s에서 P,p 와 Y,y 추출 (정규식 이용. findall)
# 4. dict 에 key , value 로 카운팅 점수 넣기

import re
def solution(s):
    answer = True
    p = re.compile('[p,P]')
    y = re.compile('[y,Y]')
    p_cnt = len(p.findall(s))
    y_cnt = len(y.findall(s))

    print(p_cnt)
    print(y_cnt)
    if p_cnt != y_cnt:
        return False
    return True

s = "Pyy"
print(solution(s))