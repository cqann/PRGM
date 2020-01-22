
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>

#include <unordered_set>
#include <vector>
#include <algorithm> 

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        auto it1 = s.begin();
        auto it2 = s.begin();
        unordered_set <char> cur_substr;
        int record = 0;

        while (it1 != s.end()){
            while (cur_substr.count(*it2)==0 && it2 != s.end()){
                cur_substr.insert(*it2);
                it2++;
            }
            record = max(record,(int) cur_substr.size());

            cur_substr.erase(*it1);
            it1++;
        }
        return record;
    }
};




int main()
{
    clock_t tStart = clock();

    string inpt = "bbbbb";
    Solution skrr;
    int x = skrr.lengthOfLongestSubstring(inpt);

    cout << x << " ";
    
    
    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
