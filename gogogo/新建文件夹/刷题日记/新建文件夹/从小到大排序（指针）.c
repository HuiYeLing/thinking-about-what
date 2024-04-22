#include<stdio.h>
int a[100];
void sort(int *b,int m);//自定义函数的声明

int main()
{
    int n,i;
    scanf("%d",&n);
for ( i = 0; i < n; i++)
    scanf("%d",&a[i]);
//排序
    sort(a,n);//数组名相当于传送整个数组
            //数组名相当于第一个数组元素的地址
            //a=&a[0]
    for ( i = 0; i < n-1; i++)
            printf("%d ",a[i]);
    printf("%d\n",a[n-1]);
    return 0;
}

void sort(int *b,int m)
{           //从小到大排序
    int j,index,k,temp;
    for ( j = 0; j < m-1; j++)
    {
        index=j;
        for ( k = j + 1; k < m; k++)
          if (a[k]<a[index])
                index=k;//index用于保存较小值的下标
            //找到本次循环的较小值
        if (index!=j)
        {
           temp=a[index];
           a[index]=a[j];
           a[j]=temp;
        }
        
    }
    
}