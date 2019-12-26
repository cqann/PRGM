
#include <iostream>
#include <cmath>
#include <math.h>
#include <utility>
#include <set>
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

//Koden är korrekt men long long är tydligen för litet :()
//Lösningen är på g, men c++ gillar tkr inte pow(x,1/3) är samma som cbrt()
//FUNKAR!! förenkling via loopar
int main()
{
    set<pair<int, int>> powers;
    int fact_a;
    for (int i = 2; i <= 100; i++)
    {
        for (int j = 2; j <= 100; j++)
        {
            int a = i;
            int b = j;
            
            for (int k = 2; k < 10; k++)
            {
                if (!isPrime(k))
                {
                    continue;
                }
                fact_a = floor(pow(a,1.0/((double)k)));
                while (pow(fact_a,k) == a)
                {
                    a = fact_a;
                    b *= k;
                    fact_a = floor(pow(a,1.0/((double)k)));
                    //printf("%d %d \n",sq_a,a);
                }   
            }
            
            
            
            

            powers.insert(make_pair(a,b));
        }
    }
    
    cout << powers.size();




}





