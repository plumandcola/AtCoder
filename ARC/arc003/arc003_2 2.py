N = int(input())

print(*sorted((input() for _ in range(N)), key = lambda s: s[::-1]), sep="\n")