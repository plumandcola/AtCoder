from collections import Counter

S = input()
T = int(input())

S_Counter = Counter(S)
if T == 1:
    print(abs(S_Counter["R"] - S_Counter["L"]) + abs(S_Counter["U"] - S_Counter["D"]) + S_Counter["?"])
elif T == 2:
    print(max(len(S) % 2, abs(S_Counter["R"] - S_Counter["L"]) + abs(S_Counter["U"] - S_Counter["D"]) - S_Counter["?"]))
