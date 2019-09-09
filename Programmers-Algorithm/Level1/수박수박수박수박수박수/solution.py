def water_melon(n):
    str = ""
    for i in range(n):
        if i % 2 == 0:
            str = str + "수"
        else:
            str = str + "박"
    return str
print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))
