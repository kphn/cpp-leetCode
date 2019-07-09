#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<vector<int>> permuteUnique(vector<int> &nums)
    {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        do
        {
            res.push_back(nums);
        } while (next_permutation(nums.begin(), nums.end()));
        return res;
    }
};

int main()
{
    Solution s;
    vector<int> nums{1, 1, 2};
    vector<vector<int>> res = s.permuteUnique(nums);

    for (auto p = begin(res); p != end(res); ++p)
    { //用begin()和end()来替代手工的控制变量
        for (auto q = begin(*p); q != end(*p); ++q)
        {
            cout << *q << ' ';
        }
        cout << endl;
    }

    return 0;
}