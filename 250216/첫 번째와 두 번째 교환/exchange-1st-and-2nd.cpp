#include <string>
#include <iostream>
using namespace std;

int main() {
    string str;

    cin >> str;
    char first, second;

    first = str[0];
    second = str[1];
    
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == first)
            str[i] = second;
        else if (str[i] == second)
            str[i] = first;
    }
    cout << str << endl;
    return 0;
}