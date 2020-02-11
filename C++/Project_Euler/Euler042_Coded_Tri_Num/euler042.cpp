
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <unordered_set>
#include <vector>
#include <fstream> 
#include <stdio.h> 
#include <string.h> 

using namespace std;

int to_val(string s){
    int result = 0;
    for (char c : s){
        int alpha_val = c - 'A' + 1;
        result += alpha_val;
    }
    return result;
}


int main()
{
    clock_t tStart = clock();
    
    unordered_set <int> tri_nums;
    int carry = 0;
    for (int i = 1; i < 10000; i++)
    {
        carry += i;
        tri_nums.insert(carry);
    }
    

    ifstream myfile;
    myfile.open("formatted.txt");

    string str;
    int res = 0;
    while (myfile >> str){
        if (tri_nums.count(to_val(str)) != 0){
            res++;
        }
    }

    
    cout << res;
    
    myfile.close();

    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
