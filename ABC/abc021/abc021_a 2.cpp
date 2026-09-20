#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, num = 1;
    cin >> N;

    vector<int> ans;
    while (N) {
        if (N & num) {
            ans.push_back(num);
            N -= num;
        }
        num <<= 1;
    }

    cout << ans.size() << endl;
    for (int num : ans) cout << num << endl;
}