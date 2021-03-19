#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

int N,ans=0;
bool check[1000] = { false, };
void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void cal() {
    
    for (int a0=1; a0 < 10; a0++) {
        if (a0 > N) break;
        else {
            check[a0] = true;
        }

        for (int d = -9; d < 10; d++) {
            string num = to_string(a0);
            int next_jari = a0 + d;
            while (next_jari > -1 && next_jari < 10) {
                num += to_string(next_jari);
                if (stoi(num) > N) break;
                else {
                    check[stoi(num)] = true;
                    next_jari = next_jari + d;
                }
            }
        }

    }


}

int main() {
    cin >> N;
    cal();
    
    //cout << check[1];
    for (int i = 1; i <= N; i++)
        if (check[i]) ans++;

    cout << ans;    
}
