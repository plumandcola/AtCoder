class Trie: #トライ木全体を表すクラス
    def __init__(self):
        self.root = Trie.Node() #トライ木の根を表す

    class Node: #トライ木の各頂点を表すクラス
        def __init__(self):
            self.child = {} #文字cをラベルとして持つ辺を通って進める頂点を表す
            self.count = 0
    
    def insert(self, word: str): #文字列wordをトライ木に格納する
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = Trie.Node()
            node = node.child[c]
            node.count += 1
    
    def get_max_lcp(self, T: str) -> str:
        result = 0
        node = self.root
        for c in T:
            if node.child[c].count <= 1:
                return result

            node = node.child[c]
            result += 1
        return result


tree = Trie()

N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    tree.insert(S[i])

for i in range(N):
    print(tree.get_max_lcp(S[i]))
