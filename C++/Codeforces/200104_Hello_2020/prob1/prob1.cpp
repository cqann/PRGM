
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>

using namespace std;

int main()
{
    clock_t tStart = clock();

    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
    return 0;
}
