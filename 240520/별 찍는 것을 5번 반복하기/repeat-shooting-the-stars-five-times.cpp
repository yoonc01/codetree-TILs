#include <iostream>
using namespace std;

void    foo()
{
    for (int i = 0; i < 10; i++)
        cout << '*';
    cout << '\n';
}
int main() {
for (int i = 0; i < 5; i++)
    foo();
    
    return 0;
}