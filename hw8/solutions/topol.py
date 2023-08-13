
#!/usr/bin/env python3

from collections import defaultdict

def _order0(n, edges): # Derek style, no need for head pointer in queue
   
    # convert list of edges to adj. list
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in edges: # u->v
        adjlist[u].append(v)
        indegree[v] += 1
        
    queue = [u for u in range(n) if indegree[u] == 0]
    for u in queue: # no need for while head < len(queue):
        yield u # next in the topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

def _order1(n, edges): # DEFAULT SOLUTION (classical textbook style): queue and head pointer
   
    # convert list of edges to adj. list
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in edges: # u->v
        adjlist[u].append(v)
        indegree[v] += 1
        
    queue = [u for u in range(n) if indegree[u] == 0]
    head = 0 # queue head pointer
    while head < len(queue):
        u = queue[head] # pop queue
        head += 1
        yield u # next in the topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

class CycleException(Exception): pass # define my own exception

def _order2(n, edges): # top-down, recursive, memoization

    def visit(v): # DFS
        if color[v] == 1: # gray
            raise CycleException("cycle detected")
        elif color[v] == 0: # white: visit (if black: return -- memoization)
            color[v] = 1 # becomes gray
            for u in prereqs[v]:
                visit(u)
            color[v] = 2 # now black; done
            out.append(v) # take this course now

    prereqs = defaultdict(list) # incoming edges
    for u, v in edges: # u->v
        prereqs[v].append(u)
    
    color = defaultdict(int) # default: white (0)
    out = [] # topological order (output)
    try:
        for u in range(n): # DFS on each non-visited node
            visit(u) # try to visit u if it's white            
    except CycleException: # important: only catch my own exception
        return out # cycle detected; out is not the whole set
    return out

def _order3(n, edges): # using stack; not required
   
    # convert list of edges to adj. list
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in edges: # u->v
        adjlist[u].append(v)
        indegree[v] += 1
        
    stack = [u for u in range(n) if indegree[u] == 0]
    while stack != []:
        u = stack.pop() # pop the last node; O(1); can't popleft which is O(n)
        yield u # next in the topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)

def order(n, edges):
    out = list(_order2(n, edges))
    return out if len(out) == n else None

if __name__ == "__main__":
    print(order(2, [(0,1), (1,0)]))
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
