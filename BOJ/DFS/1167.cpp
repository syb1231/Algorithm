#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
#include <memory.h>
#include <math.h>
#include<algorithm>
#define max_index 100000
using namespace std;

int node_count;
vector<pair<int, int>> tree_info[max_index+1];
int max_zirum = -1,the_node;
bool visit[max_index+1] = { false, };


void init_setting() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
}


void dfs(int node, int cost) {
    visit[node] = true;

    if (max_zirum < cost) {
        the_node = node;
        max_zirum = cost;
    }
    int node_size = tree_info[node].size();

    for (int index = 0; index < node_size; index++) {
        if(!visit[tree_info[node][index].first])dfs(tree_info[node][index].first,cost+tree_info[node][index].second);
    }

}


int main() {
    init_setting();

    cin >> node_count;

    for (int i = 0; i < node_count; i++) {
        int index;
        cin >> index;
        while (true) {
            int tmp;
            cin >> tmp;
            if (tmp == -1) break;
            int tmp2;
            cin >> tmp2;
            tree_info[index].push_back(make_pair(tmp, tmp2));
        }
    }

    dfs(1,0);
    memset(visit, false, sizeof(visit));
    dfs(the_node, 0);

    cout  << max_zirum << endl;
   
}
