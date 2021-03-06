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
	int size, count, ans = 0;
	cin >> size;
	cin >> count;
	vector<int> computer(size+1);

	for (int i = 1; i <= size; i++) computer[i] = i;

	for (int i = 0; i < count; i++) {
		int tmp[2];
		cin >> tmp[0] >> tmp[1];
		unionparent(computer, tmp[0], tmp[1]);
	}

	for (int i = 2; i <= size; i++) if (findparent(computer, 1, i)) ans++;
	//cout<<"check: "<< getparent(computer, 7);
	cout << ans;
}
