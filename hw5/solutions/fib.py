#!/usr/bin/env python3

import time

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    for i in range(12): #range(12,21):
        n = 2**i
        start = time.time()
        f = fib(n)        
        print("n:", n, f, "base10-digits:", len(str(f)), "time: %.6f" % (time.time() - start))
