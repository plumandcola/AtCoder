K = int(input())

print(bin(K).replace("1", "2")[2:]) #[2:]で、頭の"0b"を取り除く