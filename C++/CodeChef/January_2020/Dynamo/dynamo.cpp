
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

    int t;
    cin >> t;

    for (int test = 0; test < t; test++){
        long long N,N10,S,a,b,c,d,e;
        int verdict;
        cin >> N;
        N10 = pow(10,N);
        cin >> a;
        S = N10*2 + a ;
        cout << S << endl;
        cin >> b;
        c = N10 - b;
        cout << c << endl;
        cin >> d;
        e = N10 - d;
        cout << e << endl;

        cin >> verdict;

        if (verdict == -1) break;

        
    }
    
    
    return 0;
}
