N = int(input())
H = list(map(int, input().split()))

print(max(range(N), key = lambda i: H[i]) + 1)