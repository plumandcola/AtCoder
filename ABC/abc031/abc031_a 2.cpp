#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, D;
    cin >> A >> D;

    if (A >= D) cout << A * (D+1) << endl;
    else cout << (A+1) * D << endl;
}