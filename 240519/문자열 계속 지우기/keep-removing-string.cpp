#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;

    cin >> a >> b;
    int len_a = a.length();
    int len_b = b.length();

    while(1)
    {
        bool exists = false;
        for (int i = 0; i < len_a - len_b + 1; i++)
        {
            if (a.substr(i, len_b) == b)
            {
                a.erase(i, len_b);
                len_a = len_a - len_b;
                exists = true;
                break;
            }
        }
        if (exists)
            ;
        else
            break;
    }
    cout << a;
    return 0;
}