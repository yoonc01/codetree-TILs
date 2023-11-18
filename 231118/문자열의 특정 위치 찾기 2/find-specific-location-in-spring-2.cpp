#include <iostream>
#include <string>
using namespace std;

int main() {
	string str[5] = {"apple", "banana", "grape", "blueberry", "orange"};
	char c;
	int cnt = 0;

	cin >> c;
	for (int i = 0; i < 5; i++){
		if (str[i][2] == c || str[i][3] == c)
		{
			cout << str[i] << '\n';
			cnt++;
		}
	}
	cout << cnt;

}