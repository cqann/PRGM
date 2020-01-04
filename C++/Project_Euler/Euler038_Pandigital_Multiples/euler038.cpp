
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <set>
#include <vector>

using namespace std;

bool is_pandigital(int x){
    int relative_n = 0;

    string num_str =  to_string(x);
    int length = num_str.size();
    int control = 0;
    set <int> ctrl_set;
    for (int i = 1; i <= length; i++) ctrl_set.insert(i);

    for (char& c : num_str){
        int cur = c - '0';
        if (ctrl_set.find(cur) != ctrl_set.end()){
            control++;
            ctrl_set.erase(cur);
        }
    }

    if (control == length){
        return true;
    }
    return false;
   
}

int main()
{
    clock_t tStart = clock();
    
    int record = 0;
    
    for (int i = 1; i < 10000; i++){
        vector <int> to_mult;
        to_mult.push_back(1);
        bool c = true;
        string cur;

        for (int j = 2; j < 11; j++){

            to_mult.push_back(j);
            cur = "";
            for (auto x : to_mult){
                cur += to_string(x * i);
            }
            if (cur.size() > 9) break;
            if (cur.size() == 9){
                int cur_int = stoi(cur);
                if (is_pandigital(cur_int)){
                    record = max(record,cur_int);
                }
            }
        }

    }

    cout << record;

    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
