#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;

    map<char, int> count;
    for (char c : S) count[c]++;

    for (int i = 0; i < 6; i++) cout << count['A' + i] << (i != 5 ? " " : "\n");
}