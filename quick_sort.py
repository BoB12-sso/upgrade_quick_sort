def quick_sort(arr, first, last):
    if first >= last:
        return

    pivot = first
    i = pivot + 1
    j = last

    while i <= j:
        while i <= last and arr[i] <= arr[pivot]:
            i += 1
        while j > first and arr[j] >= arr[pivot]:
            j -= 1

        if i > j:
            arr[j], arr[pivot] = arr[pivot], arr[j]
        else:
            arr[i], arr[j] = arr[j], arr[i]

    quick_sort(arr, first, j - 1)
    quick_sort(arr, j + 1, last)