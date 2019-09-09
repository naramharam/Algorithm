def digit_reverse(n):
    list = [int(i) for i in str(n)]
    list.reverse()
    return list

print("결과 : {}".format(digit_reverse(12345)))
