#include <string>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string str;

    cin >> str;
    str[1] = 'a';
    str[str.length() - 2] = 'a';
    
    cout << str;
    return 0;
}