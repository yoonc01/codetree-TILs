#include <string>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string str;

    cin >> str;

    for (int i = 0; i < str.length(); i++)
        cout << str[i] << "\n";
    return 0;
}