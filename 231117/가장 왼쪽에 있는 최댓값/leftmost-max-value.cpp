#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, idx, max_val;
    int arr[1001];

    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];
    while(1)
    {
        max_val = INT_MIN;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] > max_val)
            {
                max_val = arr[i];
                idx = i;
            }
        }
        cout << idx + 1 << " ";
        n = idx;
        if (n == 0)
            break;
    }
    
    return 0;
}