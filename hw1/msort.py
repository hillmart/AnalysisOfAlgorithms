def mergesort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

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