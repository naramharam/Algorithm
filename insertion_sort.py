def insert_sort(array):
    for i in range(len(array)-1):
        j = i
        while array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j = j - 1

    print(array)


insert_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9])
