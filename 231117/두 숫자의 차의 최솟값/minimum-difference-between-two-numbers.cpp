#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, min_val;
    int arr[10];

    min_val = INT_MAX;
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    for(int i = 0; i < n - 1; i++)
    {
        if (arr[i + 1] - arr[i] < min_val)
            min_val = arr[i + 1] - arr[i];
    }
    cout << min_val;
}