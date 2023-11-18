#include <iostream>
#include <string>
using namespace std;

int main(){
	string str1, str2;
	int len1, len2;

	cin >> str1 >> str2;
	len1 = str1.length();
	len2 = str2.length();

	if (len1 > len2)
		cout << str1 << " " << len1;
	else if (len1 < len2)
		cout << str2 << " " << len2;
	else
		cout << "same";

}