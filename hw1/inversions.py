def merge(left, right):
    result = []
    l_idx = 0
    r_idx = 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    result += left[l_idx:]
    result += right[r_idx:]
    return result

def num_inversions(arr):
    if len(arr) < 2:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    n_inversions = num_inversions(left) + num_inversions(right)
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            i += 1
        else:
            n_inversions += len(left) - i
            j += 1
    arr[:] = merge(left, right)
    return n_inversions