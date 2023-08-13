import heapq

def kmergesort(arr, k):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into k subarrays
    subarrays = []
    subarray_size = len(arr) // k
    remainder = len(arr) % k
    start = 0
    for i in range(k):
        subarray_end = start + subarray_size + (1 if i < remainder else 0)
        subarrays.append(arr[start:subarray_end])
        start = subarray_end
    
    # Recursively sort each subarray
    sorted_subarrays = [kmergesort(subarray, k) for subarray in subarrays]
    
    # Merge the sorted subarrays
    result = []
    heap = [(subarray[0], i, 0) for i, subarray in enumerate(sorted_subarrays) if len(subarray) > 0]
    heapq.heapify(heap)
    while heap:
        val, subarray_index, val_index = heapq.heappop(heap)
        result.append(val)
        if val_index + 1 < len(sorted_subarrays[subarray_index]):
            next_val = sorted_subarrays[subarray_index][val_index + 1]
            heapq.heappush(heap, (next_val, subarray_index, val_index + 1))
    
    return result