
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <set>
#include <vector>
#include <algorithm> 

using namespace std;


int main()
{
    clock_t tStart = clock();
    int digit_c = 0;
    int cur_n = 0;
    int result = 1;
    int next_log = 0;
    while (digit_c < 1000000){
        string n_str = to_string(cur_n);
        
        for (char x : n_str){
            double log_c = log10(digit_c * 1.0);
            if (abs(log_c - next_log)  < 0.000000001){
                result *= x - '0';
                cout << x - '0' << endl;
                next_log++;
            }
            digit_c++;
        }
        cur_n++;
    }


    printf("%d", result);


    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
