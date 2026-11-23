S = input()

ans = 0
n = len(S)
for i in range(n):
    ans_i = pow(10, n-i-1) #"+"がないときの数字
    
    if i < n-1:
        ans_i += pow(2, n-i-2) * (pow(5, n-i-1) - 1) // 4
        #後ろの"+"の有無や桁数などを考慮して導かれた等比数列の和 2^(n-i-2) * (5^(n-i-1) - 1) / 4

    ans_i *= int(S[i]) * pow(2, i)
    #i+1文字目の数字 × それまでの"+"の有無
    
    ans += ans_i

print(ans)