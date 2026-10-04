#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, B, C, D, E;
    cin >> A >> B >> C >> D >> E;

    cout << max(A + D + E, B + C + E) << endl;
}