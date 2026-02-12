N = int(input())
S = list(map(int, input().split()))

ans = 0
for s in S:
    not_wrong = False
    a = 1
    while 4*a*a + 6*a <= s:
        if (s - 3*a) % (4*a + 3) == 0:
            not_wrong = True
            break
        a += 1
    
    if not_wrong == False:
        ans += 1

print(ans)