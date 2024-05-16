#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;

    cin >> str;
    int i = 0;
    while(str[i] != '\0')
    {
        cout << str[i] << "\n";
        i++;
    }
    return 0;
}