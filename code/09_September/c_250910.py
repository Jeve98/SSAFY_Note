# merge sort
def mergeSort(ls):
    # -- 분할 --
    if len(ls) == 1:
        return ls

    mid = len(ls) // 2
    left = ls[:mid]
    right = ls[mid:]

    left_list = mergeSort(left)
    right_list = mergeSort(right)

    # -- 정복 -- (이미 leaf node에 도달했다고 생각하고 구현)
    merge_list = merge(left_list, right_list)

    return merge_list


def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = mergeSort(arr)
print(arr)
print()

