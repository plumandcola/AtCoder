#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    map<string, int> populations;
    int population_total = 0;
    for (int i = 0; i < N; i++) {
        string S;
        int P;
        cin >> S >> P;
        populations[S] = P;
        population_total += P;
    }

    string ans = "atcoder";
    for (auto p : populations) {
        if (2 * p.second > population_total) ans = p.first;
    }

    cout << ans << endl;
}