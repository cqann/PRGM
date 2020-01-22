
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <vector>

using namespace std;



bool isPrime(int x){
    if (x==1) return false;
    for (int i = 2; i*i < x+1; i++) if (x%i == 0) return false;
    return true;
}

int main()
{
    clock_t tStart = clock();
    
    int count = 0;

    for (int i = 10; i < 1000000; i++){
        if (!isPrime(i)) continue;
        bool truncable = true;
        string cur = to_string(i);
        for (int j = 0; j < cur.size() && truncable; j++){
            int val1 = stoi(cur.substr(0,cur.size()-j));
            int val2 = stoi(cur.substr(j,cur.size()-j));
            if (!isPrime(val1)) truncable = false;
            if (!isPrime(val2)) truncable = false;
            
        }

        if (truncable) count+=i;
        
    }

    cout << count;

    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
