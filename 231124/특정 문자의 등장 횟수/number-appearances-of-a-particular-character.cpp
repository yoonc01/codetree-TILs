#include <iostream>
#include <string>
using namespace std;

string str;
int cnt1 = 0, cnt2 = 0;

int main() {
    cin >> str;
    for(int i = 0; i < str.length() - 1; i++){
        if (str[i] == 'e' && str[i + 1] == 'e')
            cnt1++;
        else if (str[i] == 'e' && str[i + 1] == 'b')
            cnt2++;
    }
    cout << cnt1 << " " << cnt2;
    return 0;
}