N, M = map(int, input().split())

a = []
for _ in range(M):
    k = int(input())
    a.append(list(map(int, input().split()))[::-1])

count = [[] for _ in range(N)] #それぞれの色のボールのうち、一番上にあるボールの個数と、その筒
q = [] #一番上にボールが2個ある色
for i in range(M):
    c = a[i].pop() - 1
    count[c].append(i)
    if len(count[c]) == 2:
        q.append(c)

while q:
    c = q.pop()
    for i in count[c]:
        if len(a[i]) > 0:
            c2 = a[i].pop() - 1
            count[c2].append(i)
            if len(count[c2]) == 2:
                q.append(c2)

print("Yes" if all(len(count[i]) == 2 for i in range(N)) else "No")