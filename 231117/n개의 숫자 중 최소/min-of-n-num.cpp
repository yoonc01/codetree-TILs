#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, num, cnt, min_val;
    
    cin >> n;
    min_val = INT_MAX;
    cnt = 0;
    for(int i = 0; i < n; i++)
    {
        cin >> num;
        if (num < min_val)
        {
            cnt = 1;
            min_val = num;
        }
        else if (num == min_val)
            cnt = cnt + 1;
    }
    cout << min_val << " " << cnt;
    return 0;
}