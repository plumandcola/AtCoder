A, B, C, D = map(int, input().split())

if B * C > A * D:
    print("TAKAHASHI")
elif A * D > B * C:
    print("AOKI")
else:
    print("DRAW")
