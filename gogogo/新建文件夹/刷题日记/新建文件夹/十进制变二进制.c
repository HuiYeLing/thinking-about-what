#include<stdio.h>  
void f(int n) //用于求十进制数n的二进制数
{
    int a[100];
    int i=0;
    while (n!=0)
    {
        a[i]=n%2;
        n=n/2;
        i++;
        
    }
    while (i--)
    {
        printf("%d",a[i]);
    }
    

}

int main()
{
    int x;
    scanf("%d",&x);
    f(x);
    return  0;

}
