
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <vector>

using namespace std;

int base10To2(int x){
    int cur_power = 0;
    while (pow(2,cur_power)<x) cur_power++;
    string res;
    while (cur_power>= 0){
        if (x - pow(2,cur_power) >= 0){
            res += "1";
            x -= pow(2,cur_power);
        } else {
            res += "0";
        }
        cur_power--;
    }
    int length = res.size();
    int to_return = 0;
    for (int i = 0; i < length; i++){
        to_return += (res[i]-'0') * pow(10,length-i-1);
    }
    return to_return;

}

bool isPalindrome(int x){
    string str = to_string(x);
    for (int i = 0; i < ceil(str.size()/2.0);i++){
        if (str[i] != str[str.size()-i-1]) return false;
    }
    return true;
}



int main()
{
    clock_t tStart = clock();

    int result = 0;
    for (int i = 1; i < 1000000; i++) {
        if (isPalindrome(i) && isPalindrome(base10To2(i))) result += i;
    }
    cout << result;

    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
// 1772 is the answer nähae