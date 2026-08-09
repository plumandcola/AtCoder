#include <bits/stdc++.h>
using namespace std;

int solve(const vector<int>& C, const vector<int>& p) {
    int N = p.size();
    vector<bool> front(N, true);
    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            if (C[p[j]] % C[p[i]] == 0) front[j] = !front[j];
        }
    }
    
    int sum = 0;
    for (int i = 0; i < N; i++) {
        if (front[i] == true) sum++;
    }
    return sum;
}

int main() {
    // 99点解法
    int N;
    cin >> N;
    vector<int> C(N);
    for (int i = 0; i < N; i++) cin >> C[i];
    
    double ans = 0; // 期待値 × N!
    vector<int> p;
    for (int i = 0; i < N; i++) p.push_back(i);
    do {
        ans += solve(C, p);
    } while (next_permutation(p.begin(), p.end()));

    // ansをN!で割る
    for (int i = 1; i <= N; i++) ans /= i;

    cout << fixed << setprecision(10) << ans << endl;
}