# max_wis and max_wis2 are O(n) time & space (required)
# max_wis3 is O(n) time and O(1) space (not required)
# max_wis4 is O(n^2) time & space (BAD!)

def max_wis(a): # top-down; required
    best = {-1:0, -2:0} # 0-based index
    back = {}
    n = len(a)

    def top_down(i):
        if i not in best:
            best[i] = max(top_down(i-1), top_down(i-2)+a[i])
            back[i] = best[i] == best[i-1] # True if NOT take a[i]
        return best[i]

    return top_down(n-1), solution(n-1, a, back)

def solution(i, a, back): # recursive backtracing; required; shared by max_wis and max_wis2
    if i < 0:
        return []
    return solution(i-1, a, back) if back[i] else (solution(i-2, a, back) + [a[i]])

def max_wis2(a): # bottom-up; required
    best = {-1: 0, -2: 0}
    back = {}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        back[i] = best[i] == best[i-1]
    return best[n-1], solution(n-1, a, back)

def max_wis3(a): # O(1)-space, O(n) time; with binary number (bit operations) for back; not required
    x, y = 0, 0
    back = 0
    n = len(a)
    for i in range(n):
        x, y = y, max(y, x+a[i]) # like Fibonacci (see fib.py)
        back = back << 1 | (x == y)     # or back = back * 2 + (x==y)
    return y, solution3(n-1, a, back)

def solution3(i, a, back): # backtracing for max_wis3; not required
    if i < 0:
        return []
    return solution3(i-1, a, back >> 1) if back & 1 else (solution3(i-2, a, back >> 2) + [a[i]]) # or back%2; note back>>2!

def max_wis4(a): # BAD: storing subsolutions slows it down to O(n^2)
    best = {-1: 0, -2: 0}
    path = {-1: [], -2: []}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        path[i] = path[i-1] if best[i] == best[i-1] else path[i-2] + [a[i]]
    return best[n-1], path[n-1]

if __name__ == "__main__":

    import sys, random
    sys.setrecursionlimit(1000000)

    lst = [random.randint(-1e5,1e5) for _ in range(10000)]

    from time import time
    t = time()
    a = max_wis(lst)
    print("max_wis : top-down\t", time() -t) 
    t = time()
    b = max_wis2(lst)
    print("max_wis2: bottom-up\t", time() -t) 
    t = time()
    c = max_wis3(lst)
    print("max_wis3: bit oper.\t", time() -t) 
    t = time()
    d = max_wis4(lst)
    print("max_wis4: slow (subsol)\t", time() - t)
    print(a == b == c == d) # verify result
    #print(a==b)

