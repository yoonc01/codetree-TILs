#include <iostream>
using namespace std;

void    tri_star(int n)
{
    if (n == 0)
        return ;
    tri_star(n - 1);
    for (int i = 0; i < n; i++)
        cout << "*";
    cout << '\n';
}

int main() {
    int n;
    
    cin >> n;
    tri_star(n);
    return 0;
}