#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
vector<int> ans_vector;
int rectangle_info[101][4];
bool map[101][101];
int dir_x[4] = { -1,0,1,0 };
int dir_y[4] = { 0,-1,0,1 };

int N, M,tmp,ans = 0;

void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void in_rectangle(int x1, int y1, int x2, int y2) {
    for (int y = y1; y < y2; y++) {
        for (int x = x1; x < x2; x++) {
            map[y][x] = true;
        }
    }
}

bool isin(int x, int y) {
    if (x == -1 || x == N || y == -1 || y == M) return false;
    return true;
}
void dfs(int x, int y) {
    tmp++;
    map[y][x] = true;
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dir_x[dir];
        int ny = y + dir_y[dir];
        if (isin(nx, ny) && !map[ny][nx])
            dfs(nx, ny);
    }
}

int main() {
    int K;
    cin >> M >> N >> K;
    memset(map, false, sizeof(map));
    for (int i = 0; i < K; i++) {
        for (int j = 0; j < 4; j++)
            cin >> rectangle_info[i][j];
    }

    for (int i = 0; i < K;  i++) {
        in_rectangle(rectangle_info[i][0], rectangle_info[i][1], rectangle_info[i][2], rectangle_info[i][3]);
    }

    for (int y = 0; y < M; y++) {
        for (int x = 0; x < N; x++) {
            if (!map[y][x]) {
                tmp = 0;
                ans++;
                dfs(x, y);
                ans_vector.push_back(tmp);
            }
        }
    }
    sort(ans_vector.begin(), ans_vector.end());
    cout << ans<<endl;
    for(int i=0; i<ans_vector.size(); i++){
        cout << ans_vector[i] << " ";
    }

}
