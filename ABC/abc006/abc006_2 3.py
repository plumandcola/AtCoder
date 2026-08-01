import sys
sys.setrecursionlimit(10000000)

def calc_a_i(n: int) -> int:
    if a[n] == -1:
        a[n] = (calc_a_i(n-1) + calc_a_i(n-2) + calc_a_i(n-3)) % 10007
    
    return a[n]


n = int(input())

a = [-1] * max(4, n+1)
a[1] = 0
a[2] = 0
a[3] = 1

print(calc_a_i(n))