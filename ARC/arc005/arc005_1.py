words = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]

N = int(input())

print(sum(w in words for w in input()[:-1].split()))