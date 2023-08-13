
def max_wis(arr):
    memo = dict()
    back = dict()

    def _max_wis(i):
        if i == 0:
            back[i] = True if arr[0] > 0 else False
            return max(arr[0], 0)
        if i == -1:
            back[i] = False
            return 0
        if i not in memo:
            if _max_wis(i-1) > _max_wis(i-2) + arr[i]:
                memo[i] = _max_wis(i-1)
                back[i] = 0
            else:
                memo[i] = _max_wis(i-2)+arr[i]
                back[i] = 1
        return memo[i]

    def backtrack(i):
        print(i)
        if i < 0:
            return []
        elif back[i] == 1:
            return backtrack(i-2) + [arr[i]]
        else:
            return backtrack(i-1)

    return _max_wis(len(arr)-1), backtrack(len(arr)-1)

def max_wis2(arr):
    if arr == []:
        return 0,[]
    memo = {0:max(arr[0],0), 1:max(arr[1],0)}
    back = {-1:0, 0:True if arr[0] > 0 else False, 1:True if arr[1] > 0 else False}
    for i in range(2,len(arr)):
        memo[i] = max(memo[i-1], memo[i-2] + arr[i])
        if memo[i-1] > memo[i-2] + arr[i]:
            back[i] = 0
        else: 
            back[i] = 1

    def backtrack(i):
        if i < 0:
            return []
        elif back[i] == 1:
            return backtrack(i-2) + [arr[i]]
        else:
            return backtrack(i-1)

    return memo[len(arr)-1],backtrack(len(arr)-1)

# print(max_wis2([9,10,8,5,2,4]))