#include<stdio.h>  
void f(int n,int jz) 
{
    int a[100];
    int i=0;
    while (n!=0)
    {
        a[i]=n%jz;
        n=n/jz;
        i++;
        
    }
    while (i--)
    {
        printf("%d",a[i]);
    }
    

}

int main()
{
    int jz;
    int x;
    scanf("%d%d",&x,&jz);
    f(x,jz);
    return  0;

}
