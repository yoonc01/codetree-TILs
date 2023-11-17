#include <iostream>
using namespace std;

int main() {
	int n, m, arr_1[10][10], arr_2[10][10];

	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			cin >> arr_1[i][j];
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			cin >> arr_2[i][j];
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (arr_1[i][j] == arr_2[i][j])
				cout << 0 << " ";
			else
				cout << 1 << " ";
		}
		cout << "\n";
	}
}