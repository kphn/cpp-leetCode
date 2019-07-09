#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class Solution
{
public:
    bool reorderedPowerOf2(int N)
    {
        string str_num = to_string(N);
        sort(str_num.begin(), str_num.end());
        do
        {
            if (str_num.front() == '0')
            {
                continue;
            }
            if (isPowOf2(stoi(str_num)))
            {
                return true;
            }
        } while (next_permutation(str_num.begin(), str_num.end()));
        return false;
    }
    bool isPowOf2(int N)
    {
        return !(N & (N - 1));
    }
};

int main()
{
    Solution s;
    // cout << s.reorderedPowerOf2(46) << endl;
    // cout << s.reorderedPowerOf2(10) << endl;
    if (s.reorderedPowerOf2(1))
    {
        cout << "aaaa" << endl;
    }
    else
    {
        cout << "bbbbbb" << endl;
    }

    return 0;
}