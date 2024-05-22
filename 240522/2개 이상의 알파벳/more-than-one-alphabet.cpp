#include <iostream>
#include <string>
using namespace std;

int arr[26] = {};

void    change_arr(char c)
{
    arr[c - 'a'] = arr[c - 'a'] + 1;
}

int main() {
    string str;

    cin >> str;

    for (int i = 0; i < str.length(); i++)
    {
        change_arr(str[i]);
    }
    int cnt = 0;
    for (int i = 0; i < 26; i++)
    {
        if (arr[i] != 0)
            cnt++;
    }
    if (cnt >= 2)
        cout << "Yes";
    else
        cout << "No";
    return 0;
}