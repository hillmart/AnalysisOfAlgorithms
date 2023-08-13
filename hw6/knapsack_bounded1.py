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

print(best(3, [(2, 4, 2), (3, 5, 3)])) #5
print(best(3, [(1, 5, 2), (1, 5, 3)])) #15
print(best(3, [(1, 5, 1), (1, 5, 3)])) #15
# print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])) #130
# print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])) #236