s = input()
k = int(input())

password = set()
for i in range(len(s) - k + 1):
    password.add(s[i:i+k])

print(len(password))