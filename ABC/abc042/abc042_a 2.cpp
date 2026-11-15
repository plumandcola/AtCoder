#include <bits/stdc++.h>
using namespace std;

int main() {
    map<int, int> count;
    int num;
    for (int i = 0; i < 3; i++) {
        cin >> num;
        count[num]++;
    }

    cout << (count[5] == 2 && count[7] == 1 ? "YES" : "NO") << endl;
}