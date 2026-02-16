from collections import defaultdict

count = defaultdict(int)
N = int(input())
for _ in range(N):
    S = input()
    count[S] += 1

ans = S #とりあえず最後に入力された人をansに入れておく
for s in count:
    if count[s] > count[ans]:
        ans = s

print(ans)