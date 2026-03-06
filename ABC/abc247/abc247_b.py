N = int(input())
names = [input().split() for _ in range(N)]

ans = True
for i in range(N):
    ans_i = False
    for j in range(N):
        if i != j and names[i][0] in names[j]:
            break
    else: #sがどの人にも含まれていなかった
        ans_i = True
    
    for j in range(N):
        if i != j and names[i][1] in names[j]:
            break
    else: #tがどの人にも含まれていなかった
        ans_i = True
    
    ans &= ans_i

print("Yes" if ans else "No")