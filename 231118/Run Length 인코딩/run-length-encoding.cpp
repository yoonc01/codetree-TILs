#include <iostream>
#include <string>
using namespace std;

int main(){
	string str, ans;
	cin >> str;

	ans = "";
	char pivot = str[0];
	int cnt = 1;
	for(int i = 1; i < str.length() + 1; i++){
		if (pivot == str[i])
			cnt++;
		else
		{
			ans = ans + pivot + to_string(cnt);
			pivot = str[i];
			cnt = 1;
		}
	}
	cout << ans.length() << '\n';
	cout << ans;
}