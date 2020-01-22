
#include <iostream>
#include <cmath>
#include <time.h>

#include <string>
#include <vector>
#include <utility>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

//Intressant uppgift jag tror jag har löst det då jag får korrekta svar på uppgifter. Har testat med test från tävlinge (se nedan). Enligt Kattis kör programmet inte tillräckligt snabbt, osäker på om det är ngt i min metod eller vad
//svår
struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};




pair <int,int> calcBestCut(vector <int> pos, int i1, int i2){
    // house per dis, där det är som  likast 
    // ska cuttas där kortast max distans skapas 
    int best ;
    int lowest = 10000000;
    int s_diff = 10000000;
    for (int i = i1; i <= i2-1; i++){
        double min_max1 = (pos[i]-pos[i1])/2.0;
        double min_max2 = (pos[i2]-pos[i+1])/2.0;
        
        if (abs(min_max1-min_max2) < s_diff){
            s_diff = abs(min_max1-min_max2);
            lowest = min_max1 + min_max2;
            best = i;
        }

    }

    return make_pair(lowest,best);
}



int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n_of_cases;
    cin >> n_of_cases;
    clock_t tStart = clock();

    for (int i = 0; i < n_of_cases; i++){
        int n;
        int m;
        cin >> n >> m;
        vector <int> house_pos;
        for (int h = 0; h < m; h++){    
            int to_add;                 // O(n*log n)
            cin >> to_add;
            auto bounds = lower_bound(house_pos.begin(),house_pos.end(),to_add);
            house_pos.insert(bounds,to_add);
        }
        for (auto x : house_pos) cout << x << "\n";
         
        unordered_map <pair<int,int>,pair<int,int>, pair_hash> saves;
        unordered_set <pair<int,int>, pair_hash> cuts;
        cuts.insert(make_pair(0,m-1));

        for (int i = 0; i < n-1; i++){
            //FIND WHICH PART TO CUT
            double max_dis = -1;
            pair <int,int> cut;
            for (auto c: cuts){
                if (max_dis < (c.second - c.first)/2.0){
                    max_dis = (c.second - c.first)/2.0;
                    cut = c;
                }
            }
            //FIND WHERE TO CUT
            pair <int,int> ret;
            if (saves.count(cut) == 0){            
                ret = calcBestCut(house_pos,cut.first,cut.second);
                saves[cut] = ret;
            } else {
                ret = saves[cut];
            }
            int i_to_cut = ret.second;

            //CUT
            cuts.insert(make_pair(cut.first,i_to_cut));
            cuts.insert(make_pair(i_to_cut+1,cut.second));
            cuts.erase(cut);
        }

        double closest = 0.0;
        for (auto cut : cuts){
            closest = max(closest, (house_pos[cut.second]-house_pos[cut.first])/2.0);
        }
        
        printf("%.1f\n",closest);
    }

    
    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);


    return 0;
}
/*
1
96 217
908810
176935
390226
950187
323927
275175
652100
66938
314416
7205
937081
565665
621845
143777
989916
404823
690186
405532
654029
246563
12194
549977
519970
678681
936243
809276
250441
425738
494117
990586
273168
335465
50350
735733
839392
673677
59440
247163
872948
573982
764128
838489
168156
514914
142142
246104
906458
801484
353709
813008
857246
22276
634512
751438
831158
445249
83754
799914
619831
2874
551649
357004
242902
207859
938010
180822
605524
258505
519019
577899
140026
384128
960280
171330
780251
475588
104917
678063
265951
98747
781566
681795
167759
556587
349354
682559
616700
734617
507568
748858
27467
310167
285857
2875
970153
878951
273484
656628
794110
155354
664581
971292
919839
707533
68133
501924
922592
24711
662045
130534
504547
443076
921726
387825
565351
272215
139269
65102
428074
863673
80310
599667
480370
659935
709961
780169
435819
451887
514757
530772
949917
571606
265580
14366
745987
735787
564700
65977
164473
394696
776174
915744
552773
275495
395179
957675
36076
433998
525573
780652
224601
131619
341533
629469
758465
125819
757751
478477
196384
221901
697744
844889
615294
923458
366996
817627
783006
670920
644808
735059
576063
57214
286418
503375
576864
208357
877841
284504
913839
398820
205668
775197
43800
639657
423051
467773
389856
278487
3924
41998
264094
574479
341308
417801
32048
636258
887999
461768
224027
603675
262980
396691
41498
649852
131628
681723
660700
676767
212381
257747
839419
356482
382658
964990
919646
223568
204209

*/