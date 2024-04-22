#include<stdio.h>
int main()
{   
    int a[100],n,i,j,t;
    scanf("%d",&n);
    for ( i = 0; i < n; i++)
    {
        scanf("%d",&a[i]);
    }
    for ( i = 0; i < n-1; i++)
    {
        for ( j = i+1; j <n ; j++)
        {
            if (a[i]<a[j])
            {
              t=a[i];
              a[i]=a[j];
              a[j]=t;  
            }
            
        }
        
    }
    printf("%d",a[0]);
    for ( i = 1; i < n; i++)
    {
        printf(" %d",a[i]);
    }
    
    return 0;
}