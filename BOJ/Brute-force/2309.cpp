#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int najangi[9];
vector<int> ans;

void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

bool checking(int p1, int p2) {
    int sum = 0;
    for (int i = 0; i < 9; i++) {
        if (i == p1 || i == p2)continue;
        sum += najangi[i];
    }

    if (sum == 100) {
        for (int i = 0; i < 9; i++) {
            if (i == p1 || i == p2) continue;
            ans.push_back(najangi[i]);
        }
        return true;
    }
    return false;
}

int main() {
    init_setting();
    for (int i = 0 ; i < 9; i++)
        cin >> najangi[i];

    for (int p1 = 0; p1 < 8; p1++) {
        for (int p2 = p1 + 1; p2 < 9; p2++)
            if (checking(p1, p2)) {
                sort(ans.begin(), ans.end());
                for (int i = 0; i < ans.size(); i++)
                    cout << ans[i] << endl;
                return 0;
            }
    }
   
}
