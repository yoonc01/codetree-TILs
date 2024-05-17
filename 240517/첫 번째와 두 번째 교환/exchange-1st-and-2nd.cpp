#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    int len;

    cin >> a;
    len = a.length();
    char first = a[0];
    char second = a[1];

    for (int i = 0; i < len; i++)
    {
        if (a[i] == first)
            a[i] = second;
        else if (a[i] == second)
            a[i] = first;
    }
    cout << a;
    return 0;
}