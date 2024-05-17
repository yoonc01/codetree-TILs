#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, len;
    string str;

    cin >> str >> n;
    len = str.length();
    for(int i = 0; i < n; i++)
    {
        int cmd;
        cin >> cmd;
        if (cmd == 1)
        {
            int a, b;
            char temp;
            cin >> a >> b;
            temp = str[a - 1];
            str[a - 1] = str[b - 1];
            str[b - 1] = temp;
        }
        else
        {
            char a, b;
            cin >> a >> b;
            for (int i = 0; i < len; i++)
            {
                if (str[i] == a)
                    str[i] = b;
            }
        }
        cout << str << '\n';
    }
    return 0;
}