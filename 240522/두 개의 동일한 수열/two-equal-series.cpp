#include <iostream>
#include <algorithm>

using namespace std;

int arr1[100];
int arr2[100];

bool check(int n)
{
    for (int i = 0; i < n; i++)
    {
        if (arr1[i] != arr2[i])
            return false;
    }
    return true;
}

int main() {
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr1[i];
    for (int i = 0; i < n; i++)
        cin >> arr2[i];

    sort(arr1, arr1 + n);
    sort(arr2, arr2 + n);

    if (check(n))
        cout << "Yes";
    else
        cout << "No";
            
    return 0;
}