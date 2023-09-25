# 1. money - (price*count)번... = answer
# for n in count:
#     price +(price*n)
# 2. money - answer
# 3. if money - answer >= 0 : return 0
def solution(price, money, count):
    res = 0
    for c in range(1, count+1):
        # print(c)
        n = (price*c)
        print('n번째 타고 난 후 요금 : ', n)
        res +=n
        print(c,'번째','answer:', res)

    if (money-res) >=0:
        return 0
    return abs(money-res)

print(solution(3, 20, 4))

