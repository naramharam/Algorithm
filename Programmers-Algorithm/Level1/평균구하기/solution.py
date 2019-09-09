def average(array):
    i = 0
    for j in  array:
        i = i + j

    avr = i /  len(array)

    return avr

list = [5,3,4]
print("평균값 : {}".format(average(list)))
