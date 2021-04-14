#include <iostream>
#include <vector>
#include <string>
#include <memory.h>
using namespace std;
int N;
vector<vector<int>> tree_info;
vector<int> parent_info;

void dfs(int now) {
    for (int i = 0; i < tree_info[now].size(); i++) {
        if (!parent_info[tree_info[now][i]]) {
            parent_info[tree_info[now][i]] = now;
            dfs(tree_info[now][i]);
        }
    }
}

int main() {
    cin >> N;
    tree_info.resize(N + 1);
    parent_info.resize(N + 1, 0);

    for (int i = 1; i < N; i++) {
        int tmp[2];
        cin >> tmp[0] >> tmp[1];
        tree_info[tmp[0]].push_back(tmp[1]);
        tree_info[tmp[1]].push_back(tmp[0]);
    }
    parent_info[1] = 1;
    dfs(1);
    for (int i = 2; i <= N; i++) {
        cout << parent_info[i] << "\n";
    }




}
