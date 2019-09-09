def getPrime(n):
    sum = 0
    s = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                s += 1
        if s == 0:
            sum += 1
        s = 0
    return sum

print(getPrime(10))
