#include <bits/stdc++.h>
using namespace std;

int main() {
    string W;
    cin >> W;
    for (char c : W) {
        if (c != 'a' && c != 'i' && c != 'u' && c != 'e' && c != 'o') cout << c;
    }
    cout << endl;
}