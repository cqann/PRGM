
#include <iostream>
#include <cmath>
#include <math.h>
#include <vector>

using namespace std;



int main()
{
    int result = 0;

    for (int i = 10; i < 10000000; i++)
    {
        string curNum = to_string(i);
        int curSum = 0;
        int curIntChar;
        for (int j = 0; j < curNum.size(); j++)
        {
            curIntChar = curNum[j] -'0';
            curSum += pow(curIntChar,5);
        }

        if (curSum == i){
            result += i;
        }
        
        
    }
    
    cout<<result;

    return 0;

}





