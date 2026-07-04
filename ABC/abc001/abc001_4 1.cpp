#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<bool> rain(289, false);
    /*
    雨が降っていたかどうかを記録
    rain[t] := t//12時 t%12*5分 〜 t//12時 t%12*5+4分 に雨が降っていたかどうか
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

        for (int t = S; t < E; t++) {
            rain[t] = true;
        }
    }
    
    int S = 0;
    while (S < 288) {
        if (rain[S] == true) {
            int E = S;
            while (rain[E] == true) {
                E++;
            }
            cout << format("{:02}{:02}-{:02}{:02}", S/12, S%12*5, E/12, E%12*5) << endl;
            S = E;
        } else {
            S++;
        }
    }
}