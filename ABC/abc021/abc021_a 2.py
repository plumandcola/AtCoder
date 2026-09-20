N = int(input())

ans = []
num = 1
while N:
    if N & num:
        ans.append(num)
        N -= num
    num <<= 1

print(len(ans))
for num in ans:
    print(num)
