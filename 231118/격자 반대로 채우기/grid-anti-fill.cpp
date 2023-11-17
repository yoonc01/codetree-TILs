#include <iostream>
using namespace std;

int main() {
	int n, num = 1, arr[10][10];

	cin >> n;
	for(int i = n - 1; 0 <= i; i--)
	{
		if (i % 2 == (n - 1) % 2)
		{
			for(int j = n - 1; 0 <= j; j--)
				arr[j][i] = num++;
		}
		else
		{
			for (int j = 0; j < n; j++)
				arr[j][i] = num++;
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			cout << arr[i][j] << ' ';
		cout << '\n';
	}
}