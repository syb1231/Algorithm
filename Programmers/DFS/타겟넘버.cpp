#include <string>
#include <vector>

using namespace std;

int target_real, answer=0;
vector<int> numbers_real;
void dfs(int index,int result) { // 종료 조건
    if (index == numbers_real.size()) {
        if (result == target_real) answer++;
        return;
    }
    dfs(index + 1, result + numbers_real[index]);  
    dfs(index + 1, result - numbers_real[index]);
}

int solution(vector<int> numbers, int target) {
    numbers_real.assign(numbers.begin(), numbers.end());
    target_real = target;
     dfs(0, 0);
    return answer;
}
