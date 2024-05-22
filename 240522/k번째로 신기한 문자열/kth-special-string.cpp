#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string arr[100];
string prefix;

bool check(string str, int n)
{
    for (int i = 0; i < n; i++)
        if (prefix[i] != str[i])
            return false;
    return true;
}

int main() {
    int n, m, idx = 0, len;
    string str;

    cin >> n >> m >> prefix;
    len = prefix.length();
    for (int i = 0; i < n; i++)
    {
        cin >> str;
        if (check(str, len))
        {
            arr[idx] = str;
            idx++;
        }
    }
    sort(arr, arr + idx);
    cout << arr[m - 1];
    return 0;
}