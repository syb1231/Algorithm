#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

int N,ans=0;
int start_node;
int max_length = -1;
int visited[10000];
bool check = false;
vector<pair<int, int>> node_info[100001];
void init_setting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void dfs(int node_now ,int length) {
    visited[node_now] = true;
    // 모든 노드 방문 ㄱㄱ
    for (int i = 0; i < node_info[node_now].size(); i++) {
        if (!visited[node_info[node_now][i].first]) dfs(node_info[node_now][i].first, length + node_info[node_now][i].second);
    }

    if (length > max_length) {
        start_node = node_now;
        max_length = length;
    }
}

int main() {
    int count;
    cin >> count;
    memset(visited, false, sizeof(visited));
 
    // 입력
    for (int i = 0; i < count-1; i++) {
        int tmp[3];
        cin >> tmp[0]>>tmp[1]>>tmp[2];
        node_info[tmp[0]].push_back(make_pair(tmp[1], tmp[2]));
        node_info[tmp[1]].push_back(make_pair(tmp[0], tmp[2]));
    }

    dfs(1,0);
    check = true;
    memset(visited, false, sizeof(visited));
    max_length = -1;
    dfs(start_node, 0);


    cout << max_length;    
}
