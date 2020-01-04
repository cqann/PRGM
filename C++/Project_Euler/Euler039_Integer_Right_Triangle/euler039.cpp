
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

    int ps[1001] = {0};
    int count = 0;

    for (int a = 1; a <= 1000; a++){
        for (int b = 1; b <= a; b++){
            double c = sqrt(1.0*a*a + 1.0*b*b);
            
            int roundc = round(c);
            if (roundc*roundc == a*a + b*b){
                if (roundc+b+a < 1001) {
                    ps[roundc+b+a] += 1;
                }
            }
            
        }
    }

    int record = 0;
    int best;
    for (int i = 0; i < 1001; i++){
        if (record < ps[i]){
            record = ps[i];
            best = i;
        }
    }
    cout << best;

    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
