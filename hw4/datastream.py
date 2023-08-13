import heapq

def ksmallest(k, arr):
    heap_k = []
    i = 0
    for i, x in enumerate(arr):
        if i < k:
            heapq.heappush(heap_k, -x)
        elif len(heap_k) > 0 and -x > heap_k[0]:
            heapq.heapreplace(heap_k, -x)
    return sorted([-x for x in heap_k])