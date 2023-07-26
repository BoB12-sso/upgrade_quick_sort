def upgrade_quick(arr, first, last):
    if first >= last:
        return

    # 삽입 정렬 사용하여 작은 배열 정렬 최적화
    if last - first <= 10:
        insertion_sort(arr, first, last)
        return

    # 삼중 분할 퀵소트 사용하여 피벗 선정 최적화
    pivot_index = ternary_partition(arr, first, last)

    upgrade_quick(arr, first, pivot_index - 1)
    upgrade_quick(arr, pivot_index + 1, last)

def insertion_sort(arr, first, last):
    for i in range(first + 1, last + 1):
        key = arr[i]
        j = i - 1
        while j >= first and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def ternary_partition(arr, first, last):
    mid = first + (last - first) // 2
    a, b, c = arr[first], arr[mid], arr[last]
    pivot = sorted([a, b, c])[1]

    if pivot == a:
        pivot_index = first
    elif pivot == b:
        pivot_index = mid
    else:
        pivot_index = last

    arr[pivot_index], arr[last] = arr[last], arr[pivot_index]

    i = first - 1
    for j in range(first, last):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[last] = arr[last], arr[i + 1]

    return i + 1