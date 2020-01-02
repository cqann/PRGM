
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <vector>
#include <deque>

using namespace std;


bool isPrime(int x){
    for (int i = 2; i*i < x+1; i++){
        if (x%i == 0){
            return false;
        }
    }
    return true;
}

int main()
{
    clock_t tStart = clock();

    int result = 0;

    for (int i = 2; i < 1000000; i++){
        if (!isPrime(i)) continue;

        string cur_str = to_string(i);
        deque <int> cur_wheel;
        for (auto c : cur_str) cur_wheel.push_back(c - '0');
        

        int ctrl = 0;
        for (int j = 0; j < cur_str.size(); j++){
            int to_send_back = cur_wheel[0];
            cur_wheel.pop_front();
            cur_wheel.push_back(to_send_back);
            int cur_rot = 0;
            for (int k = cur_wheel.size()-1; k >= 0; k--){
                cur_rot += cur_wheel[k] * pow(10,cur_wheel.size()-k-1);
            }

            if (isPrime(cur_rot)) ctrl++;
        }

        if (ctrl == cur_wheel.size()) result++;

    }
    
    cout << result;

    
    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
// 55 är svaret!!!
