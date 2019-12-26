#include <iostream>
#include <cmath>
#include <math.h>
#include <vector>
using namespace std;



int main()
{
   
    long long result = 1;
    int layer = 1;
    int ptsVisitedInLayer = 0;
    int ptsInLayer = pow(layer*2 + 1, 2);
    int index = 2;
    int offsetCounter = 0;
    vector <int> pts;
    while(index <= 1001*1001){

        if (ptsVisitedInLayer == ptsInLayer){
            layer++;
            ptsVisitedInLayer = 0;
            ptsInLayer = pow(layer*2 + 1,2) - pow((layer-1)*2 + 1,2) ;
            offsetCounter = 0 ;

        }

        if(index%2 == 1){
            if (offsetCounter == layer-1){
                result += index;

                pts.push_back(index);
                printf("%d %d %d, ",index, offsetCounter,layer);
                offsetCounter = 0;
            } else {
                offsetCounter += 1;
            }
        }

        ptsVisitedInLayer++;
        index++;
        
        
        
    }
    
    cout << endl << endl << result << endl;
    cout << pts.size()/8 + 1;
    return 0;

}






/*
int main()
{
    int index = 0;
    int layer = 0;
    int ptsVisitedInLayer = 0;
    int ptsInLayer = pow(layer*2 + 1,2);
    int y = 501;
    int x = 501;
    vector<vector<int>> pts;

    while(index != 1001*1001){
        vector <int> cur {x,y,index+1};
        pts.push_back(cur);
        ptsVisitedInLayer++;

        if (ptsVisitedInLayer == ptsInLayer){
            layer++;
            ptsVisitedInLayer = 0;
            ptsInLayer = pow(layer*2 + 1,2);
        }


        index++;
    }

    

    return 0;

}


*/




