#include <iostream>
#include <map>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        map<char, int> m;
        int res = 0;
        auto beg = 0;
        for (size_t i = 0; i < s.size(); i++)
        {
            auto ix = m.find(s[i]);
            if (ix == m.end() || beg > ix->second)
            {
                res = max(res, int(i - beg + 1));
            }
            else
            {
                beg = ix->second + 1;
            }
            m[s[i]] = i;
        }

        return res;
    }
};

int main()
{
    Solution s;
    cout << s.lengthOfLongestSubstring("tmmzuxt") << endl;
    // cout << s.lengthOfLongestSubstring("pwwkew") << endl;
    return 0;
}