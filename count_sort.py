def counting_sorted(arr, K):
    cnt = [0] * K
    sorted_arr = [0] * len(arr)

    for i in arr:
        cnt[i] += 1

    for i in range(1, K):
        cnt[i] += cnt[i - 1]

    for i in range(len(arr)):
        sorted_arr[cnt[arr[i]] - 1] = arr[i]
        cnt[arr[i]] -= 1

    return sorted_arr


array = [3, 5, 1, 2, 9, 6, 4, 7, 5]
print(counting_sorted(array, 20))