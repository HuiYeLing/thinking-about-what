#include<stdio.h>
#include<string.h>

int main()
{
    int n,i,j;
    int sum=0;
    int f=1;
    while (scanf("%d",&n)!=EOF)
{
    for ( i = 1; i <=n; i++)
    {
        f=1;
   for ( j = 1; j <=i; j++)
   {
   f *=j;
   }
   sum+=f;
    }
printf("%d\n",sum);
sum=0;
}   
    return 0;
}