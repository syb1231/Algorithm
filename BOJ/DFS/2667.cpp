#include <iostream>
#include<vector>
#include <functional>
#include <queue>
#include<algorithm>
using namespace std;

int map[25][25];
int wid;


void dfs(int x, int y, int &count) {
	map[y][x] = 0;
	if (x > 0 && map[y][x - 1]) dfs(x - 1, y, ++count);
	if (y > 0 && map[y - 1][x]) dfs(x , y - 1, ++count);
	if (x < wid-1 && map[y][x + 1]) dfs(x + 1, y, ++count);
	if (y < wid-1 && map[y + 1][x]) dfs(x, y + 1, ++count);
}

int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);
        cout.tie(NULL);

	int room_count = 0;
	vector<int> room;
	cin >> wid;

	for (int i = 0; i < wid; i++) { // 입력
		string tmp;
		cin >> tmp;
		for (int j = 0; j < wid; j++)
			map[i][j] = tmp[j] - '0';
	}

	for (int i = 0; i < wid; i++) { // dfs
		for(int j=0; j<wid; j++)
			if (map[i][j]) {
				room_count = 1;
				dfs(j, i, room_count);
				room.push_back(room_count);
			}
	}

	//출력 
	sort(room.begin(), room.end());
		
	cout << room.size()<<endl;
	for (int i = 0; i < room.size(); i++)
		cout << room[i] << endl;
	
}
