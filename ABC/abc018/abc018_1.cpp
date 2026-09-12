#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B >> C;

    cout << 3 - (A >= B) - (A >= C) << endl;
    cout << 3 - (B >= A) - (B >= C) << endl;
    cout << 3 - (C >= A) - (C >= B) << endl;
}