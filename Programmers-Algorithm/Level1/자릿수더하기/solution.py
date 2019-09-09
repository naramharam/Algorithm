def sum_digit(number):
	result = 0
	for i in str(number):
		result += int(i)
	return result

print("결과 : {}".format(sum_digit(123)))
