N, A, B = map(int, input().split())

ans = 0
for _ in range(N):
    s, d = input().split()
    d = int(d)

    d = max(d, A)
    d = min(d, B)
    
    if s == "West":
        d *= -1
    
    ans += d

if ans > 0:
    print("East", end=" ")
elif ans < 0:
    print("West", end=" ")

print(abs(ans))