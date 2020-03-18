
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{

    int n, q;
    cin >> n >> q;
    int days[n];
    int prev;
    bool dsc[n];
    bool asc[n];

    for (int day = 0; day < n; day++)
    {
        cin >> days[day];
        if (day == 0)
        {
            prev = days[day];
            dsc[day] = true;
            asc[day] = true;
            continue;
        }

        asc[day] = (days[day] >= prev);
        dsc[day] = (days[day] <= prev);
    }

    return 0;
}
