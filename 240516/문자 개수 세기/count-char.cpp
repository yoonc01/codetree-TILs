#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    char c;
    int ans = 0;
    
    getline(cin, str);
    cin >> c;
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == c)
            ans++;
    }
    cout << ans;
    return 0;
}