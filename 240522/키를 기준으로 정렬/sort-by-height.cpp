#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

class Person{
    public:
        string name;
        int h, w;

        Person(string name="", int h=0, int w=0){
            this->name = name;
            this->h = h;
            this->w = w;
        }
};

bool compare(const Person &a, const Person &b){
    return a.h < b.h;
}

Person people[10];

int main() {
    int n;

    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> people[i].name >> people[i].h >> people[i].w;
    }
    sort(people, people + n, compare);
    for (int i = 0; i < n; i++)
        cout << people[i].name << ' ' << people[i].h << ' ' << people[i].w << '\n';
    
    return 0;
}