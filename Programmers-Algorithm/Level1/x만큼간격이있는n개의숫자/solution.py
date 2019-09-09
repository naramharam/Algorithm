def number_generator(x, n):
    num = []
    for i in range(0,5):
        num.append(x+(i*x))

    return num

print(number_generator(3,5))
