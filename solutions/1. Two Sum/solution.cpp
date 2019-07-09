#include <iostream>
#include<tr1/unordered_map>
#include<map>
#include<vector>
#include<string>
using namespace std;
using namespace std::tr1;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>m;
        vector<int>res;
        for (size_t i = 0; i < nums.size(); i++)
        {
            if(m.find(nums[i]) == m.end()){
                m[target - nums[i]] = i;
            }else{
                res.push_back(m[nums[i]]);
                res.push_back(i);
                
                break;
            }
        }
        // cout<<res[0]<<" "<<res[1];
        return res;
    }
};

int main() 
{
    Solution s;
    vector<int>nums;
    nums.push_back(7);
    nums.push_back(2);
    nums.push_back(11);
    nums.push_back(15);
    s.twoSum(nums,9);
    return 0;
}