#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int n;
    int arr[50];
    cin >> n;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        arr[i] = abs(temp);
    }
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}