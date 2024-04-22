#include<stdio.h>
int i,j;
void f(int t)
{
 for ( i = 1; i < t/2+1; i++)
{
    for ( j = 1; j <= t/2+1; j++)
    {
        printf(" ");
    }
    for ( j = 1; j <=2*i-1; j++)
    {
        printf("*");
    }
    printf("\n");
}
    for ( i = t/2; i >= 1; i--)
    {
        for ( j = 1; j < t/2+1-i; j++)
        {
            printf(" ");
        }
        for ( i = 1; i < 2*i-1; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}

int main()
{
    int c,h;//局部变量，只能在此函数中使用
    scanf("%d",&c);
    while (c--)
    {
        scanf("%d",&h);
        f(h);
    }
    return 0;
}