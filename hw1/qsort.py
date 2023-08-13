def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def sorted(t):
    if t == []:
        return []
    else:
        return sorted(t[0]) + [t[1]] + sorted(t[2])

def _search(tree, x):
    if tree == []:
        return []
    elif x == tree[1]:
        return tree
    elif x < tree[1]:
        return _search(tree[0], x)
    else:
        return _search(tree[2], x)

def search(tree, x):
    return _search(tree, x) #!= []

def insert(tree, x):
    if not tree:
        tree.extend([[], x, []])
        return tree
    if x < tree[1]:
        if not tree[0]:
            tree[0] = [[], x, []]
            return tree[0]
        else:
            return insert(tree[0], x)
    elif x > tree[1]:
        if not tree[2]:
            tree[2] = [[], x, []]
            return tree[2]
        else:
            return insert(tree[2], x)
    return tree