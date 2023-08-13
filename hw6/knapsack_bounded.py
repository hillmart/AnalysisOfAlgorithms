# def best(W, items):
#     n = len(items)

#     # Create a table to store the maximum values
#     table = [[0] * (W + 1) for _ in range(n + 1)]

#     # Create a table to store the choices made for each item
#     choices = [[0] * (W + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         weight, value, count = items[i - 1]
#         for w in range(1, W + 1):
#             max_value = table[i - 1][w]  # Exclude the current item
#             for j in range(1, min(w // weight, count) + 1):
#                 if table[i - 1][w - j * weight] + j * value > max_value:
#                     max_value = table[i - 1][w - j * weight] + j * value
#                     choices[i][w] = j
#             table[i][w] = max_value

#     # Determine the items included in the knapsack
#     included_items = [0] * n
#     w = W
#     for i in range(n, 0, -1):
#         included_items[i - 1] = choices[i][w]
#         w -= choices[i][w] * items[i - 1][0]

#     return table[n][W], included_items

def best(W,store):
    n = len(store)
    memo = {}
    choices = {}

    def _best(w,i):
        if i < 0 or w < 0:
            return 0   
        if (w,i) not in memo:
            max_value = 0
            max_count = 0
            w_i, v_i, c_i = store[i]
            for j in range(min(w//w_i,c_i)+1):
                current_value = _best(w-j*w_i, i-1)+j*v_i
                if  current_value > max_value:
                    max_value = current_value
                    max_count = j

            memo[(w,i)] = max_value
            choices[(w,i)] = max_count

        return memo[(w,i)]

    def create_included_items(w, i):
        if i < 0:
            return []

        count = choices[(w, i)] if (w, i) in choices else 0
        rest = create_included_items(w - count*store[i][0], i - 1)
        included_items = rest + [count]

        return included_items

    return _best(W,n-1), create_included_items(W,n-1)