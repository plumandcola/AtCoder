#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N, M;
    cin >> T;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    cin >> M;
    vector<int> B(M);
    for (int i = 0; i < M; i++) cin >> B[i];

    int i = 0, j = 0; // AとBのインデックス
    while (true) {
        if (i == N || A[i] > B[j]) { // 売れるたこ焼きがない場合
            cout << "no" << endl;
            return 0;
        } else if (A[i] < B[j] - T) { // 一番古いたこ焼きが、作成されてからT秒を超えている場合
            i++;
        } else { // たこ焼きを売ることができる場合
            i++;
            j++;
        }

        if (j == M) {
            cout << "yes" << endl;
            return 0;
        }
    }
}