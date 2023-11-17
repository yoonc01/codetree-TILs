#include <iostream>
using namespace std;

int main() {
	int arr[4][4], sum = 0;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			cin >> arr[i][j];
	}
	
	for (int i = 0; i < 4; i++)
	{
		for(int j = 0; j < i + 1; j++)
			sum = sum + arr[i][j];
	}
	cout << sum;
}