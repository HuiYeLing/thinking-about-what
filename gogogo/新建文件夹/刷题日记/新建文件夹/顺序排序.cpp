#include<stdio.h>
int main()
{
    int i,j,n,m,min,dx,t,flag;
    int a[100];
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d",&m);
        for ( i = 0; i < m; i++)
        
            scanf("%d",&a[i]);//输入数组
        //将数组从小到大排序
         //有m个数，找m-1次最小值
        for ( i = 0; i < m-1; i++)
        {
            min=i;
            for ( j=i+1; j < m; j++)
                if (a[j]<a[min])
                    min=j;//找出较小值的下标
                t=a[i];
                a[i]=a[min];
                a[min]=t;
        }
        dx=a[1]-a[0];//计算等差数列的差值
        flag=0;  
        for ( i = 1; i < m; i++)
        {
            if (a[i]-a[i-1]!=dx)
            {//非等差数列
                flag=1;
                break;
            }
            
        }
            if(flag==0)
            printf("yes\n") ;
            else//不是等差数列
            printf("no\n");
    }
    return 0;
}