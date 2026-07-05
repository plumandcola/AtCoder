A, B, C, D, E = sorted(map(int, input().split()))

if (A == C and C != D and D == E) or (A == B and B != C and C == E):
    print("Yes")
else:
    print("No")
