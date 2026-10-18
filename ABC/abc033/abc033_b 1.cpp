#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<string> S(N);
    vector<int> P(N);
    int population_total = 0;
    for (int i = 0; i < N; i++) {
        cin >> S[i] >> P[i];
        population_total += P[i];
    }

    string ans = "atcoder";
    for (int i = 0; i < N; i++) {
        if (2 * P[i] > population_total) ans = S[i];
    }

    cout << ans << endl;
}