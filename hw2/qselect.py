import random

def qselect(size, arr):
    if len(arr) <= 1:
        return arr[0]
    pivot = random.randint(0, len(arr)-1)
    smaller = [x for i, x in enumerate(arr) if x < arr[pivot]]
    larger = [x for i, x in enumerate(arr) if x > arr[pivot]]
    if size == len(smaller) + 1:
        return arr[pivot]
    elif size <= len(smaller):
        return qselect(size, smaller)
    else:
        return qselect(size - len(smaller) - 1, larger)