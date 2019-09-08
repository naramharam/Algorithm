def selection_sort(array):

    for i in range(0, len(array)-1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        print(array)


array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
selection_sort(array)
