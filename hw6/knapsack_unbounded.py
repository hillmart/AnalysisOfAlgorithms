def best(W, store):
    bag = {0:0}
    back = {0:None}

    def _best(w):
        if w <= 0:
            return 0
        if w not in bag:
            bag[w] = 0
            back[w] = None
            for j in range (len(store)):
                if w-store[j][0] >= 0: 
                    bestj = _best(w-store[j][0])
                    if bestj + store[j][1] > bag[w]:
                        bag[w] = bestj + store[j][1]
                        back[w] = j
        return bag[w]

    def _back(w):
        # if w <= 0:
        #     return [0]*len(store)
        if back[w] is not None:
            val = _back(w - store[back[w]][0])
            val[back[w]] += 1
            return val
        else:
            return [0]*len(store)
    _best(W)
    #print(back)
    return bag[W], _back(W)

print(best(3, [(1, 5), (1, 5)]))
print(best(3, [(1, 2), (1, 5)]))
print(best(3, [(1, 2), (2, 5)]))
print(best(58, [(5, 9), (9, 18), (6, 12)]))
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))