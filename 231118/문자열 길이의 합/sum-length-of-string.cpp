#include <iostream>
#include <string>
using namespace std;

int main(){
	string str;
	int n;
	int len = 0, cnt = 0;

	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> str;
		len = len + str.length();
		if (str[0] == 'a')
			cnt++;
		
	}
	cout << len << ' ' << cnt;
}