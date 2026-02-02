X = input()
x_dict = {X[i]: chr(ord('a') + i) for i in range(26)}
x_dict_r = {chr(ord('a') + i): X[i] for i in range(26)}

N = int(input())
S = [input() for _ in range(N)]

T = sorted(["".join(x_dict[s_i] for s_i in s) for s in S])

print(*["".join(x_dict_r[t_i] for t_i in t) for t in T], sep = "\n")