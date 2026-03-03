S = input().split()
T = input().split()

if S == T or all(s != t for s, t in zip(S, T)):
    print("Yes")
else:
    print("No")