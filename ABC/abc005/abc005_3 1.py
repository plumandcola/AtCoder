T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

i = 0 #Aのインデックス
j = 0 #Bのインデックス
while j < M:
    if i == N or A[i] > B[j]: #売れるたこ焼きがない場合
        print("no")
        break
    
    if A[i] < B[j] - T: #一番古いたこ焼きが、作成されてからT秒を超えている場合
        i += 1
        continue
    
    #たこ焼きを売ることができる場合
    j += 1
    i += 1

else: #すべてのお客さんにたこ焼きを売れる場合
    print("yes")