S = [input() for _ in range(3)]

turn = 0
index = [0] * 3
while True:
    if index[turn] < len(S[turn]):
        next = S[turn][index[turn]]
        index[turn] += 1
        turn = ord(next) - ord('a')
    else:
        print(chr(ord('A') + turn))
        break
