#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
vector<vector<int>> relation;
bool visited[100];
int the_man;
int ans = -1;
void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void dfs(int now, int counting) {
    visited[now] = true;
    if (now == the_man) {
        ans = counting;
    }
    for (int i = 0; i<relation[now].size(); i++) {
        if (!visited[relation[now][i]]) {
            dfs(relation[now][i], counting + 1);
        }
    }
}

int main() {
    int start_man;
    int tmp;
    cin >> tmp;
    relation.resize(tmp+1);
    cin >> start_man >> the_man>>tmp;
    for (int i = 0; i < tmp; i++) {
        int tmp[3];
        cin >> tmp[0] >> tmp[1];
        relation[tmp[0]].push_back(tmp[1]);
        relation[tmp[1]].push_back(tmp[0]);
    }

    memset(visited, false, sizeof(visited));
    dfs(start_man, 0);

    cout << ans;
}
