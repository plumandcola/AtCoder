#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> rain(289, 0);
    /*
    雨が降っていたかどうかを、いもす法で記録
    rain[t] > 0 -> t//12時 t%12*5分 〜 t//12時 t%12*5+4分 に雨が降っていた
    */
    
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        string data;
        cin >> data;
        int S_h = stoi(data.substr(0, 2));
        int S_m = stoi(data.substr(2, 2));
        int E_h = stoi(data.substr(5, 2));
        int E_m = stoi(data.substr(7, 2));
        int S = 12 * S_h + S_m / 5; //切り捨て
        int E = 12 * E_h + (E_m + 4) / 5; //切り上げ

        // いもす法
        rain[S]++;
        rain[E]--;
    }
    
    int S = 0;
    while (S < 288) {
        rain[S+1] += rain[S];
        if (rain[S] > 0) {
            int E = S+1;
            while (rain[E] > 0) {
                rain[E+1] += rain[E];
                E++;
            }
            cout << format("{:02}{:02}-{:02}{:02}", S/12, S%12*5, E/12, E%12*5) << endl;
            S = E+1;
        } else {
            S++;
        }
    }
}