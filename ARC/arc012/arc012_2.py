N, v_a, v_b, L = map(int, input().split())

L *= (v_b / v_a) ** N

print(L)