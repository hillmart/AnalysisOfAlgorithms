def order(n, list_of_edges):
    # Create adjacency list representation of the directed graph
    graph = [[] for _ in range(n)]
    for edge in list_of_edges:
        src, dest = edge
        graph[src].append(dest)

    # Function to perform DFS and check for cycles
    def dfs(node, visited, stack, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, stack, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True

        stack.append(node)
        recursion_stack[node] = False
        return False

    # Perform topological sort using DFS
    def topological_sort():
        visited = [False] * n
        stack = []
        recursion_stack = [False] * n

        for node in range(n):
            if not visited[node]:
                if dfs(node, visited, stack, recursion_stack):
                    return None

        return stack[::-1]

    return topological_sort()

print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
print(order(5, []))
