def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    small = []
    big = []
    equal = []
    for value in array:
        if value < pivot:
            small.append(value)
        elif value > pivot:
            big.append(value)
        else:
            equal.append(value)

    return quick_sort(small) + equal + quick_sort(big)


print(quick_sort([3, 7, 8, 1, 5, 9, 6, 10, 2, 4]))
