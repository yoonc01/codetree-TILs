#include <iostream>
#include <climits>
using namespace std;

int main(){
    int n, arr[1001];
    int max_val;

    max_val = 0;
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];
    for(int i = 0; i < n - 1; i++)
    {
        for(int j = i + 1; j < n; j++)
        {
            if (arr[j] - arr[i] > max_val)
                max_val = arr[j] - arr[i];
        }
    }
    cout << max_val;
}