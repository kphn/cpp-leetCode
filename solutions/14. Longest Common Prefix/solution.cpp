#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.size() == 0)
        {
            return "";
        }

        int maxLen = maxCommonLength(strs);
        int pos = 0;
        for (size_t i = 0; i < maxLen; i++)
        {
            if (commonInPos(i, strs))
            {
                pos = i + 1;
            }
            else
            {
                break;
            }
        }
        return strs[0].substr(0, pos);
    }

private:
    bool commonInPos(int n, vector<string> &strs)
    {
        char s = strs[0][n];
        for (size_t i = 1; i < strs.size(); i++)
        {
            if (strs[i][n] != s)
            {
                return false;
            }
        }

        return true;
    }
    int maxCommonLength(vector<string> &strs)
    {
        int maxLen = 0xfffffff;
        for (size_t i = 0; i < strs.size(); i++)
        {
            if (strs[i].size() < maxLen)
            {
                maxLen = strs[i].size();
            }
        }
        return maxLen;
    }
};

int main()
{
    Solution s;
    vector<string> t1{""};
    vector<string> t2{"abc"};
    vector<string> t3{"flower", "flow", "filght"};
    vector<string> t4{"dog", "racecar", "car"};
    cout << s.longestCommonPrefix(t1) << endl;
    cout << s.longestCommonPrefix(t2) << endl;
    cout << s.longestCommonPrefix(t3) << endl;
    cout << s.longestCommonPrefix(t4) << endl;
    return 0;
}