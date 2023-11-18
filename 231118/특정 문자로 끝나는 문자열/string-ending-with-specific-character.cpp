#include <iostream>
#include <string>
using namespace std;

int main(){
	string str[10];
	char c;
	int cnt = 0;

	for (int i = 0; i < 10; i++)
		cin >> str[i];
	cin >> c;
	for (int i = 0; i < 10; i++)
	{
		if (str[i][str[i].length() - 1] == c)
		{
			cout << str[i] << '\n';
			cnt++;
		}
	}
	if (cnt == 0)
		cout << "None";
}