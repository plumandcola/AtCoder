N, K = map(int, input().split())

ans = 0

#3回とも異なる数字が出る場合
ans += (K-1) * (N-K) * 6

#2回Kが出る場合
ans += (N-1) * 3

#3回ともKが出る場合
ans += 1

print(ans / N / N / N)