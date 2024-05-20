#include <iostream>
using namespace std;

int foo(int a, int b)
{
    int ans = 1;
    while(b--)
    {
        ans = ans * a;
    }
    return (ans);
}
int main() {
    int a, b;

    cin >> a >> b;
    cout << foo(a, b);
    return 0;
}