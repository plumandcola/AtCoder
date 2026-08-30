import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

for p in itertools.product(*T):
    xor = 0
    for t in p:
        xor ^= t
    if xor == 0:
        print("Found")
        break
else: #排他的論理和が0になる選択肢の組み合わせがない場合
    print("Nothing")
