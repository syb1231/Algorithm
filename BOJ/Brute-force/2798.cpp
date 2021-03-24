#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int N, M;
vector<int> card_info;
vector<bool> check;
void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}
int sum(int p1, int p2, int p3) {
    return card_info[p1] + card_info[p2] + card_info[p3];
}

int main() {
    int p1, p2, p3;
    init_setting();
    cin >> N >> M;
    card_info.resize(N);
    check.resize(M+1,false);
    for (int i = 0; i < N; i++) {
        cin >> card_info[i];
    }
    for (p1 = 0; p1 < N-2; p1++) 
        for (p2 = p1+1; p2 < N - 1; p2++)
            for (p3 = p2+1; p3 < N; p3++) {
                int tmp = sum(p1, p2, p3);
                if (tmp <= M) {
                    check[tmp] = true;
                }
            }

    for (int val = M; val > 0; val--) {
        if (check[val]) {
            cout << val;
            return 0;
        }
    }
}
