#include <iostream>
#include<vector>
#include <functional>
#include <queue>
#include<algorithm>
using namespace std;


int getparent(vector<int>& parent, int x) {
    if (parent[x] == x) return x;
    return parent[x] = getparent(parent, parent[x]);
}

void unionparent(vector<int>& parent, int a, int b) {
    a = getparent(parent, a);
    b = getparent(parent, b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int findparent(vector<int>& parent, int a, int b) {
    a = getparent(parent, a);
    b = getparent(parent, b);
    if (a == b) return 1;
    else return 0;
}

int main() {
    int n, m,ans=0;
    cin >> n >> m;

    vector<int> point(n+1);
    vector<bool> check(n + 1,false);
    for (int i = 1; i < n + 1; i++) point[i] = i;
    for (int i = 0; i < m; i++) {
        int tmp[2];
        cin >> tmp[0] >> tmp[1];
        unionparent(point, tmp[0], tmp[1]);
    }

    for (int i = 1; i < n + 1; i++) check[getparent(point, i)] = true;
    for (int i = 1; i < n + 1; i++) if (check[i]) ans++;
    cout << ans;
}
