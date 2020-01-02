
#include <iostream>
#include <cmath>
#include <math.h>
#include <vector>
#include <set> 
#include <map>


using namespace std;

int curSum;
long long result = 0;
vector<int> coins;
vector<int> subset;
set <vector<int>> combos ; 



void create(int carry, vector <int> c){

    if (carry >= 200){
        if(carry == 200){      
            cout << (combos.find(c) != combos.end());
            if (combos.find(c) != combos.end()){
                result++;
                combos.insert(c);
            } else {
                result--;
            }
        }
        
    } else{
        if (carry + 50 <= 200){
            c[0]++;
            create(carry+50,c);
            c[0]--;
        } 
        if (carry + 25 <= 200){
            c[1]++;
            create(carry+25,c);
            c[1]--;
        }
        
        if (carry + 5 <= 200){
            c[2]++;
            create(carry+5,c);
            c[2]--;
        }
        if (carry + 10 <= 200){
            c[3]++;
            create(carry+10,c);
            c[3]--;
        }
        
        if (carry + 20 <= 200){
            c[4]++;
            create(carry+20,c);
            c[4]--;
        }
        if (carry + 50 <= 200){
            c[5]++;
            create(carry+50,c);
            c[5]--;
        }
        if (carry + 100 <= 200){
            c[6]++;
            create(carry+100,c);
            c[6]--;
        }
        if (carry + 200 <= 200){
            c[7]++;
            create(carry+200,c);
            c[7]--;
        }
        
    }
}

map <int,int> nextCoin = {{1, 2}, {2, 5}, {5, 10}, {10, 20},{20,50},{50,100},{100,200}};

void genNums(int carry, int curCoin){

    if (carry == 200){
        result++;
    } else if (carry < 200 && curCoin != 200){
        int limit = 200/curCoin;

        for (int i = 0; i <= limit; i++){ 
            genNums(carry + curCoin*i, nextCoin[curCoin]);
        }
    } 

}



//Jag gör något fel med functions defintions, googla när du kommer hem om det är möjligt att deiniea functions innuti main()
//fel just nu
int main()
{
    



   
    

    //dive(0,0);
    //create(0,tempC);
    genNums(0,1);

    cout << result;
    return 0;

}



 /*
    for (int i = 0; i < 200; i++) coins.push_back(1);
    for (int i = 0; i < 100; i++) coins.push_back(2);
    for (int i = 0; i < 40; i++) coins.push_back(5);
    for (int i = 0; i < 20; i++) coins.push_back(10);
    for (int i = 0; i < 10; i++) coins.push_back(20);
    for (int i = 0; i < 4; i++) coins.push_back(50);
    for (int i = 0; i < 2; i++) coins.push_back(100);
    for (int i = 0; i < 1; i++) coins.push_back(200);
*/

void dive(int k, int carry) {
    if (carry >= 200){
        if (carry == 200){
            result++; 
        } 
        
    }else if (k == coins.size()){

    } else {
        dive(k+1,carry);
        dive(k+1,carry+coins[k]);
    }
}