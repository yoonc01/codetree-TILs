#include <iostream>
using namespace std;

int main() {
    
    for(int i = 0; i < 19; i++)
    {
        for(int j = 0; j < 19; j++)
        {
            cout << (i + 1) << " * " << (j + 1) << " = " << (i + 1) * (j + 1);
            if (j % 2 == 1 || j == 18)
                cout << "\n";
            else
                cout << " / ";
        }
    }
    return 0;
}