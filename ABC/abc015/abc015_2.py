N = int(input())

s = 0 #バグの合計数
num = 0 #バグがあるソフトウェアの個数
for A in map(int, input().split()):
    if A != 0:
        s += A
        num += 1

print((s + num - 1) // num)