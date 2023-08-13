import heapq

def select(*a):
    n = len(a[0])
    k = len(a)
    top = []
    heap_k = []
    for i in range(k):
        heapq.heappush(heap_k, [a[i][0], i, 0])
    for i in range(n):
        val, arr_idx, idx = heapq.heappop(heap_k)
        top.append(val)
        if idx < n-1:
            heapq.heappush(heap_k, [a[arr_idx][idx+1], arr_idx, idx+1])
    return top