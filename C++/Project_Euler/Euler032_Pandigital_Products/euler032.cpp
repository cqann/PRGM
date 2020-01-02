
#include <iostream>
#include <cmath>
#include <math.h>
#include <vector>
#include <string>
#include <set>



using namespace std;

vector <int> factors(int num){
    vector <int> return_vec;
    for (double i = 0; i<ceil(sqrt(num));i++){
        if (abs(num/i - floor(num/i)) < 0.000000001){
            return_vec.push_back((int)i);
        }
    }
    return return_vec;
}


int is_pandigital(int product){
    int relative_n = 0;
    vector <int> factor_vec = factors(product);
    for (auto it = factor_vec.begin();it!=factor_vec.end();++it){

        int multiplicand = *it;
        int  multiplier = product/multiplicand;
        string num_str = to_string(multiplicand) + to_string(multiplier) + to_string(product);
        int length = num_str.size();
        if (length != 9) continue;
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
            relative_n = 1;
        }

    }
    int to_return = product*relative_n;
    return to_return;
}





int main()
{
    int result = 0;
    
    for (int i = 0; i<100000;i++){
        result += is_pandigital(i);
    }
    
    
    cout << result;

    return 0;

}


