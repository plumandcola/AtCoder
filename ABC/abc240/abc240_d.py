N = int(input())
a = list(map(int, input().split()))

ans = 0
cylinder = []
for i in range(N):
    ans += 1
    if len(cylinder) == 0 or cylinder[-1][0] != a[i]:
        cylinder.append([a[i], 1])
    else:
        cylinder[-1][1] += 1
        if cylinder[-1][0] == cylinder[-1][1]:
            ans -= cylinder[-1][1]
            cylinder.pop()
    
    print(ans)