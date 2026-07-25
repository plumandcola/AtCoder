#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    vector<int> cards = {1, 2, 3, 4, 5, 6};

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) swap(cards[i%5], cards[i%5 + 1]);

    for (int i = 0; i < 6; i++) cout << cards[i];
    cout << endl;
}