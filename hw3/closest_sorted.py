import bisect

def find(arr, x, k):
    front = bisect.bisect(arr, x) 
    back = front - 1
    while front - back - 1 < k:
        if front >= len(arr):
            back += -1
        elif (abs(arr[back] - x) <= abs(arr[front] - x)):
            back += -1
        else:
            front += 1
    return arr[back + 1:front]