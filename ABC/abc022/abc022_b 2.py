N = int(input())

flowers = set(int(input()) for _ in range(N))

print(N - len(flowers))