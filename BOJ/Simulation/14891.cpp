#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> topni[4];
int topni_top[4] = { 0, };
vector<pair<int, int>> rotation;

void init_setting() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
}

int index_cal(int index, int l_or_r) {
    if (l_or_r == 1) {
        if (!index) return 7;
        else return index-1;
    }
    else if(l_or_r == -1){
        if (index == 7) return 0;
        else return index+1;
    }   

    else if (l_or_r == 2) {
        if (index + 2 > 7) return index - 6;
        else return index + 2;
    }

    else if (l_or_r == -2) {
        if (index - 2 < 0) return index + 6;
        else return index - 2;
    }
}

void cal_l(int topni_number, int rotation_dir) {
    if (topni_number > 0 && topni[topni_number - 1][index_cal(topni_top[topni_number - 1], 2)] != topni[topni_number][index_cal(topni_top[topni_number], -2)]) {
        cal_l(topni_number - 1, rotation_dir * -1);
    }

    topni_top[topni_number] = index_cal(topni_top[topni_number], rotation_dir);

}

void cal_r(int topni_number, int rotation_dir) {
    if (topni_number < 3 && topni[topni_number + 1][index_cal(topni_top[topni_number + 1], -2)] != topni[topni_number][index_cal(topni_top[topni_number], 2)]) {
        cal_r(topni_number + 1, rotation_dir * -1);
    }

    topni_top[topni_number] = index_cal(topni_top[topni_number], rotation_dir);
    
}

int main() {
    init_setting();
    int ans = 0 , score = 1;

    for (int i = 0; i < 4; i++) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < 8; j++) topni[i].push_back(tmp[j] - '0');
        topni_top[i] = 0;
    }
    

    int rotation_size;
    cin >> rotation_size;

    rotation.resize(rotation_size);

    for (int i = 0; i < rotation_size; i++) {
        cin >> rotation[i].first >> rotation[i].second;
        cal_l(rotation[i].first - 1, rotation[i].second);
        topni_top[rotation[i].first - 1] = index_cal(topni_top[rotation[i].first - 1], rotation[i].second * -1);
        cal_r(rotation[i].first - 1, rotation[i].second);

    }

    for (int i = 0; i < 4; i++) {
        ans += score * (topni[i][topni_top[i]]);
        score *= 2;
    }

    cout << ans;
}
