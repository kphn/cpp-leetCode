#include <iostream>
class Solution
{
public:
    int addDigits(int num)
    {
        if (num == 0)
        {
            return 0;
        }
        if (num % 9 == 0)
        {
            return 9;
        }
        return num % 9;
    }
};

int main()
{
    Solution s;
    std::cout << s.addDigits(9) << std::endl;
    std::cout << s.addDigits(926345) << std::endl;
}