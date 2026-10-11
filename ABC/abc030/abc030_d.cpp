#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, a;
    cin >> N >> a;

    string k; // 桁数が大きいので、文字列として受け取る
    cin >> k;

    vector<int> b(N);
    for (int i = 0; i < N; i++) cin >> b[i];

    int i = a - 1;
    vector<int> min_step(N, -1);
    min_step[i] = 0;
    while (min_step[b[i] - 1] == -1) {
        min_step[b[i] - 1] = min_step[i] + 1;
        i = b[i] - 1;
    }

    int before_cycle = min_step[b[i] - 1];
    int cycle = min_step[i] + 1 - min_step[b[i] - 1];

    if (k.size() < 7 && stoi(k) < before_cycle) {
        auto it = find(min_step.begin(), min_step.end(), stoi(k));
        cout << distance(min_step.begin(), it) + 1 << endl;
    } else {
        int k_int = 0; // kが大きいので、余りをとりながら上の位から足していく
        for (int i = 0; i < k.size(); i++) {
            k_int = (10 * k_int + (k[i] - '0')) % cycle;
        }

        // 答えとなる単語に、最初に辿り着くステップ数
        k_int = ((k_int - before_cycle) % cycle + cycle) % cycle + before_cycle;
        auto it = find(min_step.begin(), min_step.end(), k_int);
        cout << distance(min_step.begin(), it) + 1 << endl;
    }
}