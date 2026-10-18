S = input() + "+" #'+'が来た時の処理が最後にも行われるように、末尾に'+'を付け加える

ans = 0
contains_0 = False
for c in S:
    if c == '0':
        contains_0 = True
    elif c == '+':
        if contains_0 == False:
            ans += 1
        else:
            contains_0 = False

print(ans)