#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	string str[3];
	int	len[3];

	for (int i = 0; i < 3; i++){
		cin >> str[i];
		len[i] = str[i].length();
	}

	cout << max(len[0], max(len[1], len[2])) - min(len[0], min(len[1], len[2]));
}