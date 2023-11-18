#include <iostream>
#include <string>
using namespace std;

int main(){
	int n;
	string ans = "", str;

	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> str;
		ans = ans + str;
	}
	for(int i = 0; i < ans.length(); i++){
		cout << ans[i];
		if (i % 5 == 4)
			cout << '\n';
	}
}