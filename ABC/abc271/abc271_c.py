N = int(input())
a = list(map(int, input().split()))

extra = 0 #重複して持っている冊数
a_set = set()
for i in range(N):
    if a[i] not in a_set:
        a_set.add(a[i])
    else:
        extra += 1

a_sorted = sorted(a_set)

ans = 0
while True:
    if ans + 1 in a_set:
        ans += 1
    elif extra >= 2:
        extra -= 2
        ans += 1
    elif extra == 1 and a_sorted and a_sorted[-1] > ans:
        extra -= 1
        a_set.remove(a_sorted[-1])
        a_sorted.pop()
        ans += 1
    elif len(a_sorted) >= 2 and a_sorted[-2] > ans:
        a_set.remove(a_sorted[-1])
        a_sorted.pop()
        a_set.remove(a_sorted[-1])
        a_sorted.pop()
        ans += 1
    else:
        break

print(ans)