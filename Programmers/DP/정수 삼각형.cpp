#include <string>
#include <vector>

using namespace std;
vector<int> init(500, -1);
vector<vector<int>> dp(500, init);


int dp_(int x, int y, vector<vector<int>> &triangle) {
    if (dp[y][x] != -1) return dp[y][x] ;
    else {
        if (x == 0) {
            return dp[y][x] = dp_(x,y - 1, triangle) + triangle[y][x];
        }
        else if (x == triangle[y].size() - 1) {
            return dp[y][x] = dp_(x - 1, y - 1, triangle) + triangle[y][x];
        }
        else {
            return dp[y][x] = max(dp_(x,y - 1, triangle), dp_(x - 1,y - 1, triangle)) + triangle[y][x];
        }
    }
    
}

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    
    dp[0][0] = triangle[0][0];

    for (int i = 0; i < triangle.size(); i++)
        if (answer < dp_(i, triangle.size() - 1, triangle) ) answer = dp_(i, triangle.size() - 1, triangle);
    return answer;
}
