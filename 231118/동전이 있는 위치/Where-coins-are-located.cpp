#include <iostream>
using namespace std;

int main() {
	int n, m, arr[10][10] = {};
	int exist;

	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int r, c;
		cin >> r >> c;
		r--;
		c--;
		arr[r][c] = 1;
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)	
			cout << arr[i][j] << " ";
		cout << '\n';
	}
}