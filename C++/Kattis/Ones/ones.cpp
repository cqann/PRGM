
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <set>
#include <vector>
#include <algorithm> 

using namespace std;



int mod(string num, int a) 
{ 
    int res = 0; 
  
    for (int i = 0; i < num.length(); i++) 
         res = (res*10 + (int)num[i] - '0') %a; 
  
    return res; 
} 

int main()
{
    string s;
    while (getline(cin,s)){
        if (s.empty()) break;
        int n = stoi(s);
        string ones = "1";
        int res = 0; 
        int i = 1;
        while (true) {
            res = (res*10 + 1) %n; 
            if (res == 0) break;
            i++;
        }      
        cout << i << "\n";
    }
    return 0;
}
