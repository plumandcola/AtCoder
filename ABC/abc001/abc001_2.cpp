#include <bits/stdc++.h>
using namespace std;

int main() {
    int m;
    cin >> m;
    if (m < 100) cout << format("{:02}", 0) << endl;
    else if (100 <= m && m <= 5000) cout << format("{:02}", m / 100) << endl;
    else if (6000 <= m && m <= 30000) cout << m / 1000 + 50 << endl;
    else if (35000 <= m && m <= 70000) cout << m / 5000 + 74 << endl;
    else if (m > 70000) cout << 89 << endl;
}