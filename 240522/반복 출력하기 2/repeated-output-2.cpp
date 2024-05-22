#include <iostream>
using namespace std;

void say_hello(int n)
{
    if (n == 0)
        return ;
    cout << "HelloWorld" << '\n';
    say_hello(n - 1);
}
int main() {
    int n;

    cin >> n;
    say_hello(n);
    return 0;
}