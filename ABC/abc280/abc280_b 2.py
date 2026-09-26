N = int(input())
S = [0] + list(map(int, input().split()))

print(*(S[i+1] - S[i] for i in range(N)))