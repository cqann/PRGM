
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <vector>


using namespace std;



int main()
{
    clock_t tStart = clock();

    vector <pair <int,int>> result_vec;
    for (int i = 10; i < 100; i++){
        string i_str = to_string(i);
        for (int j = 10; j < 100; j++){
            if (i>=j) continue;
            if (i%10==0 && j%10==0) continue;
            string j_str = to_string(j);
            if (i_str[0] == j_str[0]){
                int i1 = i_str[1] - '0';
                int j1 = j_str[1] - '0';
                if (abs((1.0*i)/j - (1.0*i1)/j1) < 0.000000001){
                    pair <int,int> to_add(i,j);
                    result_vec.push_back(to_add);
                }
            }
            if (i_str[1] == j_str[0]){
                int i0 = i_str[0] - '0';
                int j1 = j_str[1] - '0';
                if (abs((1.0*i)/j - (1.0*i0)/j1) < 0.000000001){
                    pair <int,int> to_add(i,j);
                    result_vec.push_back(to_add);
                }
            }
            if (i_str[0] == j_str[1]){
                int i1 = i_str[1] - '0';
                int j0 = j_str[0] - '0';
                if (abs((1.0*i)/j - (1.0*i1)/j0) < 0.000000001){
                    pair <int,int> to_add(i,j);
                    result_vec.push_back(to_add);
                }
            }
            if (i_str[1] == j_str[1]){
                int i0 = i_str[0] - '0';
                int j0 = j_str[0] - '0';
                if (abs((1.0*i)/j - (1.0*i0)/j0) < 0.000000001){
                    pair <int,int> to_add(i,j);
                    result_vec.push_back(to_add);
                }
            }
        }   
    }
    
    int dem = 1;
    int num = 1;
    for (auto x : result_vec){
        dem *= x.first;
        num *= x.second;
        cout << x.first <<"/"<< x.second << endl;
    }
    printf("%d %d \n", dem, num);
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);

    return 0;

}


