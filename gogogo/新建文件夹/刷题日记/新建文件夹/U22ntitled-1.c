#include <stdio.h>
 
int main() 
{
    int n=0;
    while(~scanf("%d",&n))
    {
       int i=0,j=0;
       for(i=0;i<n;i++)
       {
           for(j=0;j<n;j++)
           {
               if(j==i||j==(n-i)-1)//n-1:与i相反
               {
                   printf("*");
               }
               else
                printf(" ");
           }
           printf("\n");
       } 
    }
    return 0;
}
