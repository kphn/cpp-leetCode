#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int minPathSum(vector<vector<int>> &grid)
    {
        if (grid.empty() || grid[0].empty())
        {
            return 0;
        }
        auto m = grid.size();
        auto n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));

        dp[0][0] = grid[0][0];
        for (size_t i = 0; i < m; i++)
        {
            for (size_t j = 0; j < n; j++)
            {
                if (i == 0 && j == 0)
                {
                    continue;
                }
                if (i == 0)
                {
                    dp[i][j] = grid[i][j] + dp[i][j - 1];
                }
                else if (j == 0)
                {
                    dp[i][j] = grid[i][j] + dp[i - 1][j];
                }
                else
                {
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
        return dp[m - 1][n - 1];
    }
};

int main()
{
    Solution s;
    vector<vector<int>> test;
    vector<vector<int>> test1;
    test.push_back(vector<int>{1, 3, 1});
    test.push_back(vector<int>{1, 5, 4});
    test.push_back(vector<int>{4, 2, 1});

    cout << s.minPathSum(test) << endl;
    cout << s.minPathSum(test1) << endl;
}