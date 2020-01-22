
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <unordered_map>
#include <deque>
#include <vector>
#include <algorithm> 

using namespace std;


bool isPalindrome(deque <int> x){
    for (int i = 0; i < ceil(x.size()/2.0);i++){
        if (x[i] != x[x.size()-i-1]){
            return false;
        }
    }
    return true;
}

void pV(deque <int> a, deque <int> b, int d, int d1){
    for (auto x : a){
        cout << x << " ";
    }
    cout << "paired with ";
    for (auto x : b){
        cout << x << " ";
    }
    printf("at %d %d \n",d,d1);
}

int main()
{
    

    int t;
    cin >> t;

    for (int test = 0; test < t; test++){
        
        int N,M;
        cin >> N >> M;
        int arr[N][M];

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++){
                int to_add;
                cin >> to_add;
                arr[i][j] = to_add;
            }
        }
        
        
        
        int count = N*M;
        int max_len = (min(N,M)-1)/2;

        for (int cl = 1; cl <= max_len; cl++){

            for (int r = cl; r <= N-1-cl; r++){
                deque <int> s_a;
                for (int i = 0; i < cl*2; i++){
                    s_a.push_back(arr[r][i]);
                }
                for (int i = cl*2; i < M ; i++){
                    
                    s_a.push_back(arr[r][i]);

                    if (isPalindrome(s_a)){

                        deque <int> vs_a;
                        int m_x = i - cl;

                        for (int y = r - cl; y <= r + cl; y++){
                            vs_a.push_back(arr[y][m_x]);
                        }
                        
                        if (isPalindrome(vs_a)) count++;

                    }

                    s_a.pop_front();
                }

            }
            

        }


        printf("%d \n", count);

    }

    
    
    
    
    return 0;
}
