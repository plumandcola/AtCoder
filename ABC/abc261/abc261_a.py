L_1, R_1, L_2, R_2 = map(int, input().split())

print(max(0, min(R_1, R_2) - max(L_1, L_2)))