#include <iostream>
#include <vector>
#include <functional>
#include <queue>
#include <algorithm>
using namespace std;
int map[50][50];
int w, h,counting;

void dfs(int x, int y) {
    map[y][x] = 0;
    // 가로 세로 한칸
    if (x > 0 && map[y][x - 1]) dfs(x - 1, y);
    if (y > 0 && map[y - 1][x]) dfs(x, y - 1);
    if (x < w-1 && map[y][x + 1]) dfs(x + 1, y);
    if (y < h-1 && map[y + 1][x]) dfs(x , y + 1);
    // 대각선 전진
    if (x > 0 && y > 0  && map[y - 1][x - 1]) dfs(x - 1, y - 1);
    if (x > 0 && y < h - 1 && map[y + 1][x - 1]) dfs(x - 1, y + 1);
    if (x < w - 1 && y > 0 && map[y - 1][x + 1]) dfs(x + 1, y - 1);
    if (x < w - 1 && y < h - 1 && map[y + 1][x + 1]) dfs(x + 1, y + 1);

}
int main() {
    while (true) {

        // 입력
        cin >> w >> h;
        counting= 0;
        if (w == 0 && h == 0) break;
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) cin >> map[y][x];
        }

        // dfs
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) 
                if (map[y][x]) {
                    dfs(x, y);
                    counting++;
            }
        }

        // ans
        cout << counting << endl;

    }
    
}
