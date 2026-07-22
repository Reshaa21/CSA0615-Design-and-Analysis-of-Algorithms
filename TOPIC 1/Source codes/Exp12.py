def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    inv_count = left_inv + right_inv
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count
arr = list(map(int, input("Enter the elements separated by space: ").split()))
sorted_arr, count = merge_sort(arr)
print("Number of inversions:", count)