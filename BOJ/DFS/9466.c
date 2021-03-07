#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <math.h>
#include<algorithm>
#define max_index 100001
using namespace std;
int who[max_index];
bool visited[max_index];
int ans;
void init_setting() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
}

void cal(int node, int end) {
    ans++;
    int next = who[node];
    while (next != end) {
        ans++;
        next = who[next];
    }
    
}


void dfs(int start,int node) {
    visited[node] = true;
    
    int next = who[node];
    if (!visited[next]) dfs(start,next);
    else {
        if(next!=start)cal(start,next);
        return;
    }
}


int main() {
    init_setting();
    int T,student_count;
    cin >> T;
    for (int test_case = 0; test_case < T; test_case++) {
        ans      = 0;
        cin >> student_count;
        
        memset(visited, false, (student_count + 1) * sizeof(bool));

        for (int i = 1; i <= student_count; i++) {
            cin >> who[i];
        }

        for (int i = 1; i <= student_count; i++) {      
            if (!visited[i]) dfs(i,i);
        }


        cout << ans << endl;
    }
   
}
