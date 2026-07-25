#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> cards = {1, 2, 3, 4, 5, 6};

    int N;
    cin >> N;
    vector<vector<int>> dp(30, vector<int>(6)); // ダブリング
    dp[0] = {2, 3, 4, 5, 6, 1}; // 操作を5回行った時のカードの順番
    int n = N / 5; // 操作5回を1周期として、何周期か
    int i = 0; // 周期数が2の何乗か
    while (n) {
        if (n & 1 == 1) {
            for (int j = 0; j < 6; j++) cards[j] = dp[i][cards[j] - 1];
        }

        for (int j = 0; j < 6; j++) dp[i+1][j] = dp[i][dp[i][j] - 1];
        n >>= 1;
        i++;
    }

    // 1周期に入らなかった操作の分
    for (int i = 0; i < N%5; i++) swap(cards[i%5], cards[i%5 + 1]);

    for (int i = 0; i < 6; i++) cout << cards[i];
    cout << endl;
}