#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int R, C,ans = -1;
int map[20][20];
bool passed[91] = { false, };
int dir_x[4] = { -1,1,0,0 };
int dir_y[4] = { 0,0,-1,1 };


void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

bool isin(int x, int y) {
    if (x == -1 || y == -1 || x == C || y == R) return false;
    return true;
}

void dfs(int x, int y, int distance) {
    if (ans < distance) ans = distance;
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dir_x[dir];
        int ny = y + dir_y[dir];
        if (isin(nx, ny) && !passed[map[ny][nx]]) {
            passed[map[ny][nx]] = true;
            dfs(nx, ny, distance + 1);
            passed[map[ny][nx]] = false;
        }
    }
    
}

int main() {
    init_setting();
    cin >> R >> C;

    for (int i = 0; i < R; i++){
        string tmp(C, '\0');
        cin >> tmp;
        for (int j = 0; j < C; j++) {
            map[i][j] = (int)tmp[j];
        }
    }
    passed[map[0][0]] = true;
    dfs(0, 0,1);
    cout << ans;
}
