#include<stdio.h>
int main()
{
    int a,b,k;
    scanf("%d%d",&a,&b);
    k=a;
    a=b;
    b=k;
    printf("%d %d",a,b);
return 0;
}