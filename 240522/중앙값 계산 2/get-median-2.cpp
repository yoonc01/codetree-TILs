#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    int arr[100];

    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
        if (i % 2 == 0)
        {
            sort(arr, arr + i);
            cout << arr[i / 2] << ' ';
        }
    }
    return 0;
}