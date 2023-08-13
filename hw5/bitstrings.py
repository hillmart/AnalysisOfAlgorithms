def num_no(n):
    num = {0:1, 1:2}
    for i in range(2,n+1):
        num[i] = num[i-1] + num[i-2]
    return num[n-1]

def num_yes(n):
    return 2**n - num_no(n)