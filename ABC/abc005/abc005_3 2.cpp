#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N, M;
    cin >> T;
    cin >> N;
    deque<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    cin >> M;
    deque<int> B(M);
    for (int i = 0; i < M; i++) cin >> B[i];

    while (!B.empty()) {
        if (A.empty() || A[0] > B[0]) { // 売れるたこ焼きがない場合
            cout << "no" << endl;
            return 0;
        } else if (A[0] < B[0] - T) { // 一番古いたこ焼きが、作成されてからT秒を超えている場合
            A.pop_front();
        } else { // たこ焼きを売ることができる場合
            A.pop_front();
            B.pop_front();
        }

        if (B.empty()) {
            cout << "yes" << endl;
            return 0;
        }
    }
}