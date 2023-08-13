def longest(n, list_of_edges):
    # Create adjacency list representation of the directed graph
    graph = [[] for _ in range(n)]
    for edge in list_of_edges:
        src, dest = edge
        graph[src].append(dest)

    # Perform topological sort
    def topological_sort():
        visited = [False] * n
        stack = []

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)

        for node in range(n):
            if not visited[node]:
                dfs(node)

        return stack[::-1]

    # Get the topological order
    order = topological_sort()

    # Initialize longest path length and predecessor arrays
    longest_path = [float('-inf')] * n
    predecessor = [-1] * n

    # Update longest path for each node in the topological order
    for node in order:
        if longest_path[node] == float('-inf'):
            longest_path[node] = 0
        for neighbor in graph[node]:
            if longest_path[neighbor] < longest_path[node] + 1:
                longest_path[neighbor] = longest_path[node] + 1
                predecessor[neighbor] = node

    # Find the maximum path length and the corresponding path
    max_length = max(longest_path)
    max_node = longest_path.index(max_length)
    path = []
    while max_node != -1:
        path.append(max_node)
        max_node = predecessor[max_node]

    return max_length, path[::-1]
