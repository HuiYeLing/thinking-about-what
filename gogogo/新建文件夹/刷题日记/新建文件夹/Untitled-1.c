#include<stdio.h>
#include<math.h>
int main()
{
    int x,i;
    scanf("%d",&x);
    if (x< 1)
    {
        return 0;
    }

    for( i = 2; i <=sqrt(x); i++)
    {
        if (x%i==0)
        {
            printf("%d ",i);
            x/=i;
        }

    }
    if (x>sqrt(x))
    {
       printf("%d",x);
    }
    return 0;
}