#include <iostream>
using namespace std;

int main() {
	int n, m, arr[100][100], num = 0;

	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		if (i % 2 == 0)
		{
			for(int j = 0; j < n; j++)
				arr[j][i] = num++;
		}
		else
		{
			for (int j = 0; j < n; j++)
				arr[n - j - 1][i] = num++;
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			cout << arr[i][j] << " ";
		cout << "\n";
	}
}