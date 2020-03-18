
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;
class Solution
{
public:
    int myAtoi(string str)
    {
    }
};

int main()
{
    clock_t tStart = clock();

    string inpt = "567";
    Solution skrr;
    vector<int> res = skrr.twoSum(inpt, 6);

    for (auto x : res)
    {
        cout << x << " ";
    }

    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
    return 0;
}
