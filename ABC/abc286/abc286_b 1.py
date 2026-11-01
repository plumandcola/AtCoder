N = int(input())
S = input()

i = 0
while i < N:
    if i < N-1 and S[i] == 'n' and S[i+1] == 'a':
        print("nya", end="")
        i += 2
    else:
        print(S[i], end="")
        i += 1
print() #改行