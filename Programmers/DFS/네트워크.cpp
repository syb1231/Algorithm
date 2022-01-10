#include <string>
#include <vector>

using namespace std;


int n_real,answer = 0;
vector<bool> check;

void dfs(vector<vector<int>> &computers, vector<bool> &check,int end_index, int now_index) {
    if (now_index == end_index) return;
    for (int index = 0; index < n_real; index++) {
        if (computers[now_index][index] && !check[index]) {
            check[index] = true;
            dfs(computers,check,end_index, index);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    n_real = n;
    vector<bool> check(n);
    for (int index = 0; index < n; index++) {
        if (check[index]) continue;
        answer++;
        check[index] = true;
        for (int i=0; i<computer.size(); i++) {
            if (computers[index][i]) {
                check[i] = true;
                dfs(computers, check,index, i);
            }
        }
    }
    return answer;
}
