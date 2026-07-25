S = input()

pins = [False] * 7 #pins[i] := 左からi列目に、立っているピンがあるかどうか
pins[0] = (S[6] == '1')
pins[1] = (S[3] == '1')
pins[2] = (S[1] == '1' or S[7] == '1')
pins[3] = (S[0] == '1' or S[4] == '1')
pins[4] = (S[2] == '1' or S[8] == '1')
pins[5] = (S[5] == '1')
pins[6] = (S[9] == '1')

ans = "No"
if S[0] == '0':
    for i in range(5):
        for j in range(i+2, 7):
            if (pins[i] == True) and (pins[j] == True) and (False in pins[i:j]):
                ans = "Yes"

print(ans)