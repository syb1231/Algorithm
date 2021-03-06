#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
#include <memory.h>
using namespace std;
bool check[100][100];
int map[100][100];
int depth = 0;
int xy;

void init_function() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
}


void dfs(int x, int y) {
    check[y][x] = true;

    if (x > 0 && !check[y][x - 1] && map[y][x - 1] > depth) dfs(x - 1, y);
    if (y > 0 && !check[y - 1][x] && map[y - 1][x] > depth) dfs(x, y - 1);
    if (x < xy - 1 && !check[y][x + 1] && map[y][x + 1] > depth) dfs(x + 1, y);
    if (y < xy- 1 && !check[y + 1][x] && map[y + 1][x] > depth) dfs(x, y + 1);
}

int main() {
    init_function();

    cin >> xy;
    int ans = 0;

    // 입력
    for (int i = 0; i < xy; i++) {
        for (int j = 0; j < xy; j++) {
            cin >> map[i][j];
            if (map[i][j] > depth) depth = map[i][j];
        }
    }


    // 모든 depth 에서 dfs
    while (!(depth<0)) {
        // 방문, count 초기화
        int count = 0;
        memset(check,false,sizeof(check));

        for (int i = 0; i < xy; i++) {
            for (int j = 0; j < xy; j++)
                if (map[i][j] > depth && !check[i][j]) {
                    count++;
                    dfs(j, i);
                }
        }

        if (ans < count) {
             ans = count;
        }

        depth--;
    }
   
    cout << ans << endl;
    
}
