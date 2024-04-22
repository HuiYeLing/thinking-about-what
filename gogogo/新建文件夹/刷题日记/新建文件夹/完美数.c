#include <stdio.h>
int main()
{
    int m,n,i,j,s,flag;
    while(scanf("%d%d",&m,&n),m||n)
    {
        flag=0;
        for(i=m;i<=n;i++)
        {
            s=0;
            for(j=1;j<i;j++)
            if(i%j==0)
            s=s+j;
        if(i==s)
        {
            flag=1;
            printf("%d ",i);
        }
     }
     if(flag==0)
     printf("No");
     printf("\n");
    }
    return 0;
}
