#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;

    cout << (*(S.end() - 1) == 'T' ? "YES" : "NO") << endl;
}