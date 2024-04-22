#include <stdio.h>
int gys(int n1,int n2)
{
    if (n2==0)
    {
        return n1;
    }
    else
        return gys(n2,n1%n2);
}
int main() 
{
    int  n1,n2;
    scanf("%d%d",&n1,&n2);
    int r=gys(n1,n2);
    printf("%d\n",r);
    
    return 0;
}