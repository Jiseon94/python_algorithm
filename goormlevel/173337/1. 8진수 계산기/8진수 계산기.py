def sol(numbers) :
	total = sum(numbers)
	# print(total)
	answer = format(total, 'o')
	
	return answer

N = input().strip()
numbers = list(map(int, input().split()))
print(sol(numbers))