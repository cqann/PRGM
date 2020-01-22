
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

        int s;
        int w[3];
        cin >> s >> w[0] >> w[1] >> w[2];

        if (w[2] < w[0]) {
            reverse(w,w+3);
        }

        int n_hits = 1;
        int index = 0;
        int temp_s = s;
        while (index < 3){
            if (temp_s - w[index] >= 0){
                temp_s -= w[index];
                index++;
            } else {
                temp_s = s;
                n_hits++;
            }
        }

        cout << n_hits << "\n";
    }
    
    
    return 0;
}
