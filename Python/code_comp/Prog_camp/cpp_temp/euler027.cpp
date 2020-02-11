#include <iostream>
#include <cmath>
#include <math.h>
#include <vector>
using namespace std;

bool isPrime(int n){
    int i = 2;
    while (i < ceil(sqrt(n)))
    {
        if(n%i == 0){
            return false;
        }
        i++;
    }
    return true;
}

int main()
{
    int record = 0;
    int bestA;
    int bestB;

    for (int a = -1000; a <= 1000; a++)
    {
        for (int b = -1000; b <= 1000; b++)
        {
            
            int cur;
            int n = -1;
            do
            {
                n++;
                cur = n*n + a*n + b;
            } while (isPrime(abs(cur)));
            
            if (record < n)
            {
                record = n;
                bestA = a;
                bestB = b;
            }
            
        }
        cout << a << endl;
    }
    
    cout << bestA << endl;
    cout << bestB;
   
    
    return 0;

}







