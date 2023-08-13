def distance1(s, t):
    m = len(s)
    n = len(t)

    # Create a table to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]


def distance2(s, t):
    from heapq import heappop, heappush

    m = len(s)
    n = len(t)

    # Create a priority queue (min heap) to store the states
    pq = [(0, 0, 0)]  # (cost, i, j)
    visited = set()

    while pq:
        cost, i, j = heappop(pq)

        if (i, j) in visited:
            continue

        visited.add((i, j))

        if i == m and j == n:
            return cost

        if i < m and j < n and s[i] == t[j]:
            heappush(pq, (cost, i + 1, j + 1))
        else:
            if i < m:
                heappush(pq, (cost + 1, i + 1, j))  # deletion
            if j < n:
                heappush(pq, (cost + 1, i, j + 1))  # insertion
            if i < m and j < n:
                heappush(pq, (cost + 1, i + 1, j + 1))  # substitution

    return -1  # No path found