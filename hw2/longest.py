def _longest(tree):
    if tree[0] == [] and tree[2] == []:
        return (0, 0)
    else:
        l_left = (0,0)
        l_right = (0,0)
        if tree[0] != []:
            l_left = _longest(tree[0])
        if tree[2] != []:
            l_right = _longest(tree[2])
        if tree[0] != [] and tree[2] != []:
            length = max(l_left[1] + l_right[1] + 2, l_left[0], l_right[0])
        if tree[0] == [] or tree[2] == []:
            length = max(l_left[1] + l_right[1] + 1, l_left[0], l_right[0])
        height = max(l_left[1] + 1, l_right[1] + 1)
        return (length, height)

longest = lambda tree: _longest(tree)[0]


# def longest_path(tree):
#     def dfs(tree):
#         if tree == []:
#             return (0,0)
#         left_len, left_height = dfs(tree[0])
#         right_len, right_height = dfs(tree[2])
#         length = max(left_len, right_len, left_height + right_height + 1)
#         height = max(left_height + 1, right_height + 1)
#         return length, height
        
#     return max(dfs(tree)) - 1
