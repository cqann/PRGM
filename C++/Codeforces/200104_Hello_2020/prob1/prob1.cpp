
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <set>
#include <vector>
#include <algorithm> 

using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector <int> n_copy = nums;
        sort(n_copy.begin(),n_copy.end());
        int fp = 0;
        int sp = n_copy.size()-2;
        bool bullseye = false;
        vector <int> return_vec;

        while (fp != n_copy.size() && !bullseye){
            while (n_copy[fp] + n_copy[sp] > target){
                sp--;
            }
            if (n_copy[fp] + n_copy[sp] == target && fp != sp){
                bool finpt = false;
                bool sinpt = false;
                int banned = -1;

                for (int i = 0; i < nums.size(); i++){
                    if (!finpt){
                        if (nums[i] == n_copy[fp]){
                            return_vec.push_back(i);
                            banned = i;
                            finpt = true;

                        } 
                    }
                    if (!sinpt){
                        if (nums[i] == n_copy[sp] && i != banned){
                            return_vec.push_back(i);
                            sinpt = true;
                        } 
                    }
                    
                }
                bullseye = true;
            }

            fp++;
        }

        return return_vec;
        

    }
};




int main()
{
    clock_t tStart = clock();

    vector <int> inpt = {3,3};
    Solution skrr;
    vector <int> res = skrr.twoSum(inpt,6);

    for (auto x: res){
        cout << x<<" ";
    }
    
    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
