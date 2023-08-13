__author__ = "liang huang"

# two version: heapdict (decrease_key) or heapq (duplicates in heap)
from heapdict import heapdict 
from priority_dict import priority_dict
from pqdict import pqdict
from collections import defaultdict
from heapq import heappush, heappop
import random
import time

INFTY = float("inf")

# O((V+E) log V) -- using an indexed priority queue and decrease_key
def shortest(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges:
        edges[u].append((v, cost))
        edges[v].append((u, cost))

    t = time.time()
    
    h = priority_dict() #heapdict()
    
    h[0] = 0 # alternatively, you can also set everything else to +inf
    back = {}
    popped = set() # those already popped (i.e., black nodes)
    pops = pushes = 0 # (optional) statistics
    best = defaultdict(lambda: INFTY) # current distance estimates
    while h: #len(h) > 0:
        v, d = h.popitem()
        pops += 1
        popped.add(v) # v becomes black
        if v == n-1: # target is popped (fixed)
            print("with decrease-key: time %.2f secs, V %d, E %d, pushes+decreasekeys %d, pops %d" % (time.time() - t, n, len(_edges), pushes, pops))
            return d, solution(v, back)
        for (u, cost) in edges[v]:
            newd = d + cost
            if newd < best[u]: # works for nodes of all colors
                pushes += 1
                best[u] = newd
                h[u] = newd # automatic decrease-key()
                back[u] = v 
    return None # target is not reachable

# O((E+E) log E) -- using heapq, duplicates in heap
def shortest_heapq(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges:
        edges[u].append((v, cost))
        edges[v].append((u, cost))

    t = time.time()
    
    h = [(0, 0)] # (value, node)
    best = defaultdict(lambda: INFTY)
    best[0] = 0
    popped = set() # black nodes
    back = {} # backpointers
    pushes = pops = dups = 0 # (optional) statistics
    while h: #len(h) > 0:
        d, v = heappop(h)
        pops += 1
        if v not in popped: # the first time v turns black
            popped.add(v)
            if v == n-1: # target is popped (fixed)
                print("without decrease-key: time %.2f secs, V %d, E %d, pushes %d, pops %d, dups %d" % (time.time() - t, n, len(_edges), pushes, pops, dups))
                return d, solution(v, back)
            for (u, cost) in edges[v]:
                newd = d + cost
                if newd < best[u]: # only push if u can be improved
                #if u not in popped: # BAD (only checking u is not black yet)
                    pushes += 1
                    best[u] = newd
                    back[u] = v
                    heappush(h, (newd, u)) # possibly duplicate
        else: # duplicate pop
            dups += 1
    return None # target is not reachable


#shortest = shortest_heapq # use heapq version

def solution(v, back):
    if v == 0:
        return [0]
    return solution(back[v], back).__iadd__([v])

if __name__ == "__main__":
    print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])) # unreachable

    def generate_seq(n, num_edges, seed): 
        random.seed(seed)
        return [tuple(sorted(random.sample(range(n), 2)) + [random.randint(100,1000)]) for _ in range(num_edges)]

    #dense = generate_seq(1000, 5000, 1)
    #print(shortest(1000, dense)) # (25, [0, 331, 301, 728, 999])
    #print(shortest_heapq(1000, dense)) # (25, [0, 331, 301, 728, 999])

    big = generate_seq(5000, 400000, 1)
    print(shortest(5000, big)) # 
    print(shortest_heapq(5000, big)) # 


    #print(shortest(1000, [(0, 89, 10), (0, 221, 5), (0, 301, 20), (0, 331, 5), (0, 404, 16), (0, 728, 21), (0, 999, 27), (89, 728, 11), (89, 999, 16), (221, 382, 5), (221, 331, 5), (301, 331, 7), (301, 728, 8), (301, 999, 15), (331, 404, 7), (331, 473, 8), (331, 496, 10), (332, 534, 10), (331, 999, 30), (728, 996, 9), (996, 999, 5), (728, 999, 5)]))
    
    #print(shortest(8, [(0,4,2), (0,1,7), (0,7,12), (1,2,1), (1,3,1), (1,7,5), (2,3,3), (2,4,1), (2,5,1), (2,7,10), (3,6,2), (3,4,5), (3,7,1)]))
