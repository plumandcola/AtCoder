import numpy

S = input()

ans = numpy.array([[0], [int(S[0])], [1]])
mod = 998244353
for i in range(1, len(S)):
    ans = numpy.array([[2, 1, 0], [0, 10, 2 * int(S[i])], [0, 0, 2]]) @ ans
    ans %= mod
ans = numpy.array([[1, 1, 0]]) @ ans
ans %= mod

print(ans[0][0])
