#include <iostream>
#include <vector>
#include <functional>
#include <queue>
#include<algorithm>
using namespace std;
int map[50][50];
int m, n;
void dfs(int x, int y) {
	map[y][x] = 0;

	if (x > 0 && map[y][x - 1]) dfs(x - 1,y);
	if (x < m-1 && map[y][x + 1]) dfs(x + 1, y);
	if (y > 0 && map[y - 1][x]) dfs(x, y - 1);
	if (y < n-1 && map[y + 1][x]) dfs(x, y + 1);

}


int main() {
	int T, k;
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		int ans = 0;
		cin>> m >> n >> k;
		for (int i = 0; i < k; i++) {
			int tmp[2];
			cin >> tmp[0] >> tmp[1];
			map[tmp[1]][tmp[0]] = 1;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				
				if (map[i][j]) {
					ans++;
					dfs(j, i);
				}
			}
		}

		cout << ans<<endl;
	}
}
