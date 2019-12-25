#include <iostream>
#include <cmath>
#include <vector>
using namespace std;



long long raiseToPower(long long a, long long b){
    long long result = 1;
    for (int i = 0; i < b; i++){
        result *= a;
    }
    return result;
}

int main()
{
    
    vector<long long> v;

    for (int i = 0; i < 20; i++)
    {
        v.push_back(raiseToPower(i,i+2));
    }
    
    for (int i = 0; i < v.size(); i++)
    {
        cout << v.at(i) << endl;
    }
    
    
    return 0;

}