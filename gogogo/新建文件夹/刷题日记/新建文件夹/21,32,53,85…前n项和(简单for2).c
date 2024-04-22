#include <stdio.h>
int main()
{
    int i,n;
    float sum=0,a,b,c;
        a=2;
        b=1;
        c=0;
        n=0;
    scanf("%d",&n);
        for(i=1;i<=n;i++)
    {
        sum+=a/b;
        c=a;
        a+=b;
        b=c;
    }
    printf("%.3f",sum);
	return 0;
}