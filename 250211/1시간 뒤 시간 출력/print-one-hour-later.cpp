#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int h, m;
    cin >> h >> m;
    h++;
    cout << h <<":" << m << endl;
    return 0;
}