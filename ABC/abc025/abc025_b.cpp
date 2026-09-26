#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, B, d, ans = 0;
    string s;

    cin >> N >> A >> B;
    for (int i = 0; i < N; i++) {
        cin >> s >> d;

        d = max(d, A);
        d = min(d, B);

        if (s == "West") d *= -1;

        ans += d;
    }

    if (ans > 0) cout << "East ";
    else if (ans < 0) cout << "West ";

    cout << abs(ans) << endl;
}