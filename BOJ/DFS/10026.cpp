#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int N;
bool blind;
int dir_x[4] = {0, 0, 1, -1};
int dir_y[4] = {-1, 1, 0, 0};
char map[100][100];
bool visited[100][100];
void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

bool isin(int x, int y) {
    if (x == -1 || x == N || y == -1 || y == N) return false;
    return true;
}
void dfs(int x, int y, char color) {
    visited[y][x] = true;

    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dir_x[dir];
        int ny = y + dir_y[dir];
        // 다음 갈려는 곳 체크
        if (isin(nx, ny) && !visited[ny][nx]) {
            // 맹인이고 색이 r또는 g일경우
            if (blind && !(color == 'B')) {
                if (!(map[ny][nx] == 'B'))
                    dfs(nx, ny, color);
            }
            // 맹인이 아니거나 색이 B일경우
            else {
                if (color == map[ny][nx])
                    dfs(nx, ny, color);
            }
        }
    }
}


int main() {
    init_setting();
    int blind_count = 0, normal_count = 0;
    cin >> N;
    for (int i = 0; i < N; i++) {
        string tmp(N, '\0');
        cin >> tmp;
        for (int j = 0; j < N; j++)
            map[i][j] = tmp[j];
    }
    memset(visited, false, sizeof(visited));

    // 일반인 먼저
    blind = false;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            if (!visited[y][x]) {
                normal_count++;
                dfs(x, y, map[y][x]);
            }
        }
    }
    // 방문 초기화

    memset(visited, false, sizeof(visited));
    
    // 이후 적록색약
    blind = true;

    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            if (!visited[y][x]) {
                blind_count++;
                dfs(x, y, map[y][x]);
            }
        }
    }
    cout << normal_count << " " << blind_count;
}
