#include <iostream>
#include <string>
using namespace std;

string str;
int i = 0;
int cnt;
int len = 0;

int main() {
    cin >> str;

    while(str[i] != '\0')
    {
        char c = str[i];
        cnt = 0;
        while(str[i] != '\0' && str[i] == c)
        {
            cnt++;
            i++;
        }
        len++;
        while(cnt)
        {
            len++;
            cnt = cnt / 10;
        }
    }
    cout << len << '\n';
    i = 0;
    while(str[i] != '\0')
    {
        char c = str[i];
        cnt = 0;
        while(str[i] != '\0' && str[i] == c)
        {
            cnt++;
            i++;
        }
        cout << c << cnt;
    }
    
    return 0;
}