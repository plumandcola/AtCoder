n = int(input())

ans = float("inf")
for i in range(1, n+1):
    j = n // i
    if j < i:
        break
    
    ans = min(ans, abs(i - j) + (n - i * j))

print(ans)