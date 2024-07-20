def sol(N, coin) :
	cnt = 0
	coin.sort(reverse = True)
	# print(coin)
	
	for c in coin :
		cnt += (N // c)
		# print("cnt : ", cnt)
		N = (N % c)
		# print("N : ", N)
	
	return cnt

N = int(input())
coin = [1, 40, 20, 10, 5]
# print(N)
print(sol(N, coin))

