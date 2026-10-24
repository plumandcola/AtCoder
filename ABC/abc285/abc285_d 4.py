from collections import defaultdict

class UnionFind():
    def __init__(self):
        self.parents = defaultdict(str)
        """各要素の親要素の番号を格納するリスト、要素が根（ルート）の場合は空文字列を格納する"""
    
    def find(self, s: str) -> str:
        """要素sが属するグループの根を返す"""
        if self.parents[s] == "": #根
            return s
        else:
            self.parents[s] = self.find(self.parents[s]) #経路圧縮
            return self.parents[s]

    def union(self, s: str, t: str):
        """要素sが属するグループと要素tが属するグループとを併合する"""
        s = self.find(s)
        self.parents[t] = s


ans = "Yes"
uf = UnionFind()
N = int(input())
for _ in range(N):
    S, T = input().split()
    if uf.find(S) == T:
        ans = "No"
        break
    else:
        uf.union(S, T)

print(ans)