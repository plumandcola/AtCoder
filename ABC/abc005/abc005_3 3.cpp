#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N, a, M, b;
    cin >> T;
    
    cin >> N;
    queue<int> A;
    for (int i = 0; i < N; i++) {
        cin >> a;
        A.push(a);
    }

    cin >> M;
    queue<int> B;
    for (int i = 0; i < M; i++) {
        cin >> b;
        B.push(b);
    }

    while (!B.empty()) {
        if (A.empty() || A.front() > B.front()) { // 売れるたこ焼きがない場合
            cout << "no" << endl;
            return 0;
        } else if (A.front() < B.front() - T) { // 一番古いたこ焼きが、作成されてからT秒を超えている場合
            A.pop();
        } else { // たこ焼きを売ることができる場合
            A.pop();
            B.pop();
        }

        if (B.empty()) {
            cout << "yes" << endl;
            return 0;
        }
    }
}