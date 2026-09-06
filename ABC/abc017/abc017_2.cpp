#include <bits/stdc++.h>
using namespace std;

int main() {
    string X;
    cin >> X;

    for (int i = 0; i < X.size(); i++) {
        if (X[i] == 'o' || X[i] == 'k' || X[i] == 'u') continue;
        if (X[i] == 'c' && i+1 < X.size() && X[i+1] == 'h') continue;
        if (X[i] == 'h' && i-1 >= 0 && X[i-1] == 'c') continue;

        cout << "NO" << endl;
        return 0;
    }

    cout << "YES" << endl;
}