import heapq

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
                heapq.heappush(heap, (count_pairs(structure), structure))
                return

            if dp_matrix[i][j] == dp_matrix[i][j - 1]:
                generate_structures(i, j - 1, structure + '.')
            
            for k in range(i, j):
                if dp_matrix[i][j] == dp_matrix[i][k - 1] + dp_matrix[k + 1][j - 1] + 1:
                    new_structure = structure[:k - i] + '(' + structure[k - i:j - i] + ')' + structure[j - i:]
                    generate_structures(i, k - 1, new_structure)
                    generate_structures(k + 1, j - 1, new_structure)

        generate_structures(1, n - 1, '.' * n)
        return heap   

    return heapq.nlargest(kbestk, find_all_structures(sequence, N))

sequence = "AGGCAUCAAACCCUGCAUGGGAGCG"
structures = kbest(sequence, 5)
print(structures)

def find_next_best(sequence, dp_matrix, first_structure):
    n = len(sequence)
    best_structure = None
    best_score = -1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if dp_matrix[i][j] > best_score and first_structure != dp_matrix[i][j]:
                best_score = dp_matrix[i][j]
                best_structure = dp_matrix[i][j]

    return best_structure

sequence = "AGGCAUCAAACCCUGCAUGGGAGCG"
dp_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7],
    [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 7],
    [0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6],
    [0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6],
    [0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

first_structure = '(.(.(((..))))'

# next_best_structure = find_next_best(sequence, dp_matrix, first_structure)
# print(next_best_structure)