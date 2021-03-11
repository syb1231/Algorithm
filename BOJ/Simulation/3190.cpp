#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <algorithm>
#define in_apple 1
#define in_baam -1
#define in_empty 0
#define INT_MAX 2147483647;
using namespace std;
// dir 북 서 남 동 
// dir 0  1  2  3
int N,apple_count,time_count = 0;
int map[101][101];
int dir_x[4] = {0,1,0,-1};
int dir_y[4] = { -1,0,1,0 };
vector<pair<int, char>> swap_;
queue<pair<int, int>> baam;

void init_setting() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
}

bool isin(int x, int y) {
    if (x == 0 || x == N || y == 0 || y == N) return false;
    else return true;
}

int change_dir(int dir, char l_or_r) {
    if (l_or_r == 'L') {
        if (dir == 0) return 3;
        else return dir-1;
    }
    else {
        if (dir == 3) return 0;
        else return dir+1;
    }
}

void cal(int x, int y,int dir) {
    int swap_index = 0;
    int swap_time = swap_[swap_index].first;

    while (true) {
        if (swap_time == time_count) {
            dir = change_dir(dir, swap_[swap_index].second);
            if (++swap_index < swap_.size())
                swap_time = swap_[swap_index].first;
            else swap_time = INT_MAX;
        }

        int next_x = baam.back().second + dir_x[dir];   
        int next_y = baam.back().first + dir_y[dir];

        if (isin(next_x, next_y)) {
            if (map[next_y][next_x] == in_empty) {
                map[baam.front().first][baam.front().second] = in_empty;
                baam.pop();
                
                baam.push(make_pair(next_y, next_x));
                map[baam.back().first][baam.back().second] = in_baam;
                time_count++;
                continue;
            }
            else if (map[next_y][next_x] == in_apple) {
                baam.push(make_pair(next_y, next_x));
                map[baam.back().first][baam.back().second] = in_baam;
                map[next_y][next_x] = in_empty;
                time_count++;
                continue;
            }
            else if(map[next_y][next_x] == in_baam){
                return;
            }
        }
        else return;
    }
   
}

int main() {
    init_setting();
    int swap_count;
    baam.push(make_pair(1, 1));
    
    cin >> N >> apple_count;
    N++;
    for (int i = 1; i < 101; i++) {
        memset(map[i], in_empty, sizeof(int) * 100); //모든 값 0으로 초기화
    }

    map[1][1] = in_baam;
    for (int i = 0; i < apple_count; i++) {
        int tmp[2];
        cin >> tmp[0] >> tmp[1];
        map[tmp[0]][tmp[1]] = in_apple;
    }

    cin >> swap_count;
    swap_.resize(swap_count);
    
    for (int i = 0; i < swap_count; i++) {
        char tmp;
        int tmp2;
        cin >> tmp2 >> tmp;
        swap_[i] = make_pair(tmp2, tmp);
    }
   
    cal(1,1,1);

    cout << time_count+1;
    return 0;
}
