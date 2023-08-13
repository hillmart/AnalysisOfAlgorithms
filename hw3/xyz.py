def find(unsorted):
    arr = sorted(unsorted)
    res = []
    for z in unsorted:
        back = 0
        front = len(arr) - 1
        while back != front:
            if arr[back] + arr[front] == z:
                res.append([arr[back], arr[front], z])
                back += 1
            elif arr[back] + arr[front] < z:
                back += 1
            elif arr[back] + arr[front] > z:
                front -= 1
    return res