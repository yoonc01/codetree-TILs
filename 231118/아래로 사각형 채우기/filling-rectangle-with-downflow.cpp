#include <iostream>
using namespace std;

int main() {
	int n, arr[10][10], num = 1;
	cin >> n;

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
			arr[j][i] = num++;
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			cout << arr[i][j] << ' ';
		cout << "\n";
	}
}