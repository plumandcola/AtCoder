#include <bits/stdc++.h>
using namespace std;

int main() {
    long long H, W, N, a, b;
    cin >> H >> W >> N;

    map<pair<long long, long long>, long long> count_black;
    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        for (long long h : {a-2, a-1, a}) {
            for (long long w : {b-2, b-1, b}) {
                if (1 <= h && h <= H-2 && 1 <= w && w <= W-2) count_black[{h, w}]++;
            }
        }
    }

    vector<long long> count(10, 0);
    for (auto [p, c] : count_black) count[c]++;

    count[0] = (H-2) * (W-2);
    for (long long i = 1; i < 10; i++) count[0] -= count[i];

    for (long long i = 0; i <= 9; i++) cout << count[i] << endl;
}