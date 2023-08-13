def bsts(n):
    num = {0:1, 1:1}
    for i in range(2, n+1):
        num[i] = 0
        for j in range(0, i):
            num[i] += num[j] * num[i-j-1]
    return num[n]