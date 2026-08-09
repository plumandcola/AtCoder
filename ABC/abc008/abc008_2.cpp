#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    map<string, int> count;
    string S;
    for (int i = 0; i < N; i++) {
        cin >> S;
        count[S]++;
    }

    string ans = "";
    for (const auto& p : count) {
        if (count[p.first] > count[ans]) ans = p.first;
    }

    cout << ans << endl;
}