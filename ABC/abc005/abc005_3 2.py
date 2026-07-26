from collections import deque

T = int(input())
N = int(input())
A = deque(map(int, input().split()))
M = int(input())
B = deque(map(int, input().split()))

while B:
    if len(A) == 0 or A[0] > B[0]: #売れるたこ焼きがない場合
        print("no")
        break
    
    if A[0] < B[0] - T: #一番古いたこ焼きが、作成されてからT秒を超えている場合
        A.popleft()
        continue
    
    #たこ焼きを売ることができる場合
    A.popleft()
    B.popleft()

else: #すべてのお客さんにたこ焼きを売れる場合
    print("yes")