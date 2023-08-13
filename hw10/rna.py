import heapq

def best(sequence):
    n = len(sequence)
    N = [[0] * (n+1) for _ in range(n+1)]
    back = [[None] * (n+1) for _ in range(n+1)]

    for j in range(1, n+1):
        for i in range(j, 0, -1):
            N[i][j] = N[i][j-1]
            back[i][j] = -1

            for k in range(i, j):
                if (sequence[k-1] == 'A' and sequence[j-1] == 'U') or (sequence[k-1] == 'U' and sequence[j-1] == 'A') or \
                   (sequence[k-1] == 'C' and sequence[j-1] == 'G') or (sequence[k-1] == 'G' and sequence[j-1] == 'C') or \
                   (sequence[k-1] == 'G' and sequence[j-1] == 'U') or (sequence[k-1] == 'U' and sequence[j-1] == 'G'):
                    if (N[i][j] < N[i][k-1] + N[k+1][j-1] + 1):
                        N[i][j] = N[i][k-1] + N[k+1][j-1] + 1
                        back[i][j] = k

    def traceback(i, j):
        if (back[i][j] is None):
            return ''
        elif (back[i][j] == -1):
            return traceback(i,j-1) + '.'
        else:
            k = back[i][j]
            return traceback(i,k-1) + '(' + traceback(k+1, j-1) + ')'

               
    return N[1][n], traceback(1,n)


def total(sequence):
    n = len(sequence)
    N = [[1] * (n+1) for _ in range(n+1)]

    for j in range(1, n+1):
        for i in range(j, 0, -1):
            N[i][j] = N[i][j-1]

            for k in range(i, j+1):
                if (sequence[k-1] == 'A' and sequence[j-1] == 'U') or (sequence[k-1] == 'U' and sequence[j-1] == 'A') or \
                   (sequence[k-1] == 'C' and sequence[j-1] == 'G') or (sequence[k-1] == 'G' and sequence[j-1] == 'C') or \
                   (sequence[k-1] == 'G' and sequence[j-1] == 'U') or (sequence[k-1] == 'U' and sequence[j-1] == 'G'):
                    N[i][j] += N[i][k-1] * N[k+1][j-1]

    return N[1][n]

def kbest(sequence,kbestk):
    n = len(sequence)
    N = [[0] * (n+1) for _ in range(n+1)]
    back = [[None] * (n+1) for _ in range(n+1)]

    for j in range(1, n+1):
        for i in range(j, 0, -1):
            N[i][j] = N[i][j-1]
            back[i][j] = -1

            for k in range(i, j):
                if (sequence[k-1] == 'A' and sequence[j-1] == 'U') or (sequence[k-1] == 'U' and sequence[j-1] == 'A') or \
                   (sequence[k-1] == 'C' and sequence[j-1] == 'G') or (sequence[k-1] == 'G' and sequence[j-1] == 'C') or \
                   (sequence[k-1] == 'G' and sequence[j-1] == 'U') or (sequence[k-1] == 'U' and sequence[j-1] == 'G'):
                    if (N[i][j] < N[i][k-1] + N[k+1][j-1] + 1):
                        N[i][j] = N[i][k-1] + N[k+1][j-1] + 1
                        back[i][j] = k

    def traceback(i, j):
        if (back[i][j] is None):
            return ''
        elif (back[i][j] == -1):
            return traceback(i,j-1) + '.'
        else:
            k = back[i][j]
            return traceback(i,k-1) + '(' + traceback(k+1, j-1) + ')'

    output = []

    def count_pairs(structure):
        left_paren_count = 0
        pairs_count = 0

        for char in structure:
            if char == '(':
                left_paren_count += 1
            elif char == ')':
                if left_paren_count > 0:
                    pairs_count += 1
                    left_paren_count -= 1

        return pairs_count

    # for i in range(kbestk):
    #     struct = traceback(1,n)
    #     N[1][n] -= 1
    #     output.append((count_pairs(struct), struct))
    # print(N)

    def find_all_structures(sequence, dp_matrix):
        n = len(sequence)
        heap = []

        def generate_structures(i, j, structure):
            if i >= j:
                heapq.heappush(heap, (count_pairs(structure),structure))
                return

            if dp_matrix[i][j] == dp_matrix[i][j - 1]:
                generate_structures(i, j - 1, structure + '.')
            
            for k in range(i, j):
                if dp_matrix[i][j] == dp_matrix[i][k - 1] + dp_matrix[k + 1][j - 1] + 1:
                    new_structure = structure[:k - i] + '(' + structure[k - i:j - i - 1] + ')' + structure[j - i - 1:]
                    generate_structures(i, k - 1, new_structure)
                    generate_structures(k + 1, j - 1, new_structure)

        generate_structures(1, n - 1, '.' * n)
        return heap   

    return heapq.nlargest(kbestk, find_all_structures(sequence, N))

s = "ACAGU"
# print(kbest(s, 1))  # Output: [(2, '((.))')]
# print(kbest(s, 2))  # Output: [(2, '((.))'), (1, '(...)')]
# print(kbest(s, 3))  # Output: [(2, '((.))'), (1, '(...)'), (1, '.(.).')]

print(best("AGGCAUCAAACCCUGCAUGGGAGCG"))
