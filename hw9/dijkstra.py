from heapdict import heapdict

def shortest(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    distances = {node: float('inf') for node in range(n)}
    distances[0] = 0

    queue = heapdict()
    queue[0] = 0

    while queue:
        current_node, current_distance = queue.popitem()

        if current_node == n - 1:
            # Reached the target node
            path = construct_path(distances, n, graph)
            return current_distance, path

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue[neighbor] = distance

    return None

def construct_path(distances, n, graph):
    path = []
    current_node = n - 1
    while current_node != 0:
        path.append(current_node)
        for neighbor, weight in graph[current_node]:
            if distances[current_node] == distances[neighbor] + weight:
                current_node = neighbor
                break
    path.append(0)
    return path[::-1]