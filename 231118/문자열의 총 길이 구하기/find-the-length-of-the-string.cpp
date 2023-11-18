#include <iostream>
#include <string>
using namespace std;

int main(){
	string str[10];
	int sum_val = 0;
	for(int i = 0; i < 10; i++){
		cin >> str[i];
		sum_val = sum_val + str[i].length();
	}
	cout << sum_val;
}