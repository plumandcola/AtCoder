S = input()

ans = 0
n = len(S)
for b in range(1 << (n-1)):
    formula = ""
    for i in range(n):
        formula += S[i]
        if (b >> i) & 1:
            formula += "+"
    ans += sum(map(int, formula.split('+')))

print(ans)