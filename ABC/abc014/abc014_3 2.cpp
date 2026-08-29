#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int n, a, b;
    cin >> n;

    vector<int> s(1000002, 0); // いもす法
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        s[a]++;
        s[b+1]--;
    }

    int ans = 0; // 最も人気のある濃さの色
    for (int i = 0; i < 1000001; i++) {
        if (s[i] >= s[ans]) ans = i;
        s[i+1] += s[i];
    }

    cout << s[ans] << endl;
}