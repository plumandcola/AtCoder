N = int(input())
A = sorted((a, i+1) for i, a in enumerate(map(int, input().split())))

print(A[-2][1])