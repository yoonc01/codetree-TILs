#include <iostream>
#include <string>
using namespace std;

int main(){
	string str[20];
	int sum_val = 0, cnt = 0, n;
	char c;

	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> str[i];

	cin >> c;

	for (int i = 0; i < n; i++)	{
		if (str[i][0] == c){
			cnt++;
			sum_val = sum_val + str[i].length();
		}
	}
	printf("%d %.2lf", cnt, (double)sum_val / cnt);
}