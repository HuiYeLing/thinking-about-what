#include<stdio.h>
int main()
{
    int n,i;
    scanf("%d",&n);
    char a[n+1];
       scanf("%s",a);
    for(i=0;i<n;i++)
    {             
        if('a'<=a[i]&&a[i]<='z')
        {
            a[i]-=32;
        }
      else if
        ('A'<=a[i]&&a[i]<='Z')
        {
            a[i]+=32;
        }
        else
        printf("%c",a);
        }
    for ( i = 0; i < n; i++)
    {
        printf("%c",a[i]);
    }
    return 0;
} 