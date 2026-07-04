N = int(input())

rain = [False] * 289
"""
雨が降っていたかどうかを記録
rain[t] := t//12時 t%12*5分 〜 t//12時 t%12*5+4分 に雨が降っていたかどうか
"""

for _ in range(N):
    T = input()
    S_h = int(T[0:2])
    S_m = int(T[2:4])
    E_h = int(T[5:7])
    E_m = int(T[7:9])

    S = 12 * S_h + S_m // 5 #切り捨て
    E = 12 * E_h + (E_m + 4) // 5 #切り上げ
    for i in range(S, E):
        rain[i] = True

S = 0
while S < 288:
    if rain[S] == True:
        E = S
        while rain[E] == True:
            E += 1
        print(f"{S//12:02}{S%12*5:02}-{E//12:02}{E%12*5:02}")
        S = E
    else:
        S += 1