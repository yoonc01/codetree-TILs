#include <iostream>
using namespace std;

int main() {
    int s, e;
    int sum_val, cnt = 0;

    cin >> s >> e;
    for (int i = s; i <= e; i++)
    {
        sum_val = 0;
        for (int j = 1; j < i; j++)
        {
            if (i % j == 0)
                sum_val = sum_val + j;
        }
        if (sum_val == i)
            cnt++;
    }
    cout << cnt;
    return 0;
}