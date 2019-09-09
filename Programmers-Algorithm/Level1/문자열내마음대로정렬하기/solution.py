def strange_sort(strings, n):
    strings.sort(key=lambda x: x[n])
    return strings


print(strange_sort(["sun", "bed", "car"], 1))
