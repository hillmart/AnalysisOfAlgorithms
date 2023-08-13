import heapq
import random
from random import randint

def qselect(k, a):
    index = randint(0, len(a)-1) # randomized pivot position
    a[0], a[index] = a[index] , a[0] # swap pivot with a[0]
    pivot = a[0]
        
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    left_size = len(left)+1 # including pivot
    if k == left_size:
        return pivot
    return qselect(k, left) if k < left_size else qselect(k - left_size, right)

def nbesta(a, b):
    pairs = [(x,y) for x in a for y in b]
    pairs.sort(key=lambda pair: (pair[0] + pair[1], pair[1]))
    return pairs[:len(a)]

def nbestb(a,b):
    pairs = [(x, y) for x in a for y in b]
    pairs = qselect(len(a), pairs)
    # pairs = [((pair[0] - pair[1]), pair[1]) for pair in pairs]
    # pairs = [(a[pair[0]], b[pair[1]]) for pair in pairs]
    return pairs

def nbestc(a,b):
    a.sort()
    b.sort()
    heap = [(a[0]+b[0],0,0)]
    seen = set((0,0))
    pairs = []
    while len(pairs) < len(a) and heap:
        _, i, j = heapq.heappop(heap)
        pairs.append((a[i], b[j]))
        if i+1 < len(a) and (i+1, j) not in seen:
            heapq.heappush(heap, (a[i+1]+b[j], i+1, j))
            seen.add((i+1, j))
        if j+1 < len(b) and (i, j+1) not in seen:
            heapq.heappush(heap, (a[i]+b[j+1], i, j+1))
            seen.add((i, j+1))
    return pairs
