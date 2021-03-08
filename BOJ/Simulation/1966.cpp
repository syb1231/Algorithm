#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <algorithm>

using namespace std;
int ans;

void init_setting() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
}

void cal(queue<int>& que,  vector<int> &value_vector,int the_index) {
    while (!que.empty()) {
        if (value_vector.back() == que.front()) {
            ans++;
            value_vector.pop_back();
            que.pop();
            if (the_index) the_index--;
            else return;
        }
        else {
            int tmp = que.front();
            que.pop();
            que.push(tmp);

            if (!the_index) the_index = que.size() - 1;
            else the_index--;
            
        }
    }
}


int main() {
    init_setting();
    int T;
    cin >> T;

    for (int test_case = 0; test_case < T; test_case++) {
        int que_counting,the_index,origin_size;
        vector<int> value_vector;
        queue<int> que;
        ans = 0;
        cin >> que_counting >> the_index;

        // 입력
        for (int i = 0; i < que_counting; i++) {
            int tmp;
            cin >> tmp;
            value_vector.push_back(tmp);
            que.push(tmp);
        }
        
        // 벡터정렬
        origin_size = que.size();
        sort(value_vector.begin(), value_vector.end());

        //계산
        cal(que, value_vector, the_index);
        
        // 원래 사이즈 - 현재 사이즈
        cout << origin_size-que.size() << endl;
    }
    return 0;
}
