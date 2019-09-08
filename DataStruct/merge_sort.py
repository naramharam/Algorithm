def merge_sorted(new_array):
    if len(new_array) > 1:
        mid = len(new_array) // 2
        left = new_array[:mid]
        right = new_array[mid:]
        new_left = merge_sorted(left)
        new_right = merge_sorted(right)
        return merge(new_left, new_right)
    else:
        return new_array


def merge(left, right):
    i = 0
    j = 0
    result = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while (j < len(right)):
        result.append(right[j])
        j += 1

    return result


array = [3, 5, 1, 2, 9, 6, 4, 5, 7]
print(merge_sorted(array))