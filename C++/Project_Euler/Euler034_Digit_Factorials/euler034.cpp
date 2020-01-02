
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <vector>

using namespace std;

const int n = 50000;
bool ready[n];
int vals[n];

int factorial(int x){
    if (x==0) return 1;
    if (!ready[x]){
       vals[x] =  x * factorial(x-1);
       ready[x] = true;
    }
    return vals[x];
}

int main()
{
    clock_t tStart = clock();

    int result = 0;
    
    for (int i = 3; i < n; i++)
    {
        int ph = i;
        int cur = 0;
        while (ph >= 1){
            int cur_digit = ph - (ph/10)*10;
            cur += factorial(cur_digit);
            ph /= 10;
        }
        if (cur == i) result += i;
    }
    
    cout<< result;
    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);

    return 0;

}
// 40730 är svaret!!!

