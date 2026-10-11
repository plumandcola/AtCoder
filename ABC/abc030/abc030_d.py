N, a = map(int, input().split())
k = input() #桁数が大きいので、文字列として受け取る
b = list(map(int, input().split()))

i = a - 1
min_step = [-1] * N
min_step[i] = 0
while min_step[b[i] - 1] == -1:
    min_step[b[i] - 1] = min_step[i] + 1
    i = b[i] - 1

before_cycle = min_step[b[i] - 1]
cycle = min_step[i] + 1 - min_step[b[i] - 1]

if len(k) < 7 and int(k) < before_cycle:
    print(min_step.index(int(k)) + 1)
else:
    k_int = 0 #kが大きいので、余りをとりながら上の位から足していく
    for i in range(len(k)):
        k_int = (10 * k_int + int(k[i])) % cycle
    
    #答えとなる単語に、最初に辿り着くステップ数
    k_int = (k_int - before_cycle + cycle) % cycle + before_cycle
    print(min_step.index(k_int) + 1)
