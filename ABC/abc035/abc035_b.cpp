#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    int T;
    cin >> S >> T;

    map<char, int> count;
    for (char c : S) count[c]++;

    if (T == 1) cout << abs(count['R'] - count['L']) + abs(count['U'] - count['D']) + count['?'] << endl;
    else if (T == 2) cout << max((int)(S.size() % 2), abs(count['R'] - count['L']) + abs(count['U'] - count['D']) - count['?']) << endl;
}