#include <stdio.h>

int on(int n)
{
    if (n % 2 == 0)
        return (0);
    else if (n % 10 == 5)
        return (0);
    else if (n % 3 == 0 && n % 9 != 0)
        return (0);
    return (1);
}

int main() {
    int a, b, cnt = 0;

    scanf("%d %d", &a, &b);
    for (int i = a; i < b + 1; i++)
        if (on(i))
            cnt++;
    printf("%d", cnt);
    return 0;
}