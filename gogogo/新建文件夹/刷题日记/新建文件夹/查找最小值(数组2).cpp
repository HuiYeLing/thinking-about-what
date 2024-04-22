#include<stdio.h>
 int main()
 {
    int m;  //数组的个数
    scanf("%d",&m);     //读入数组的个数
    while (m--) //用while循环对数组进行遍历
    {
        int n;  //定义整数个数
        scanf("%d",&n); //读入整数个数
int min=0;  //记录最小值
int i;  //和下面的for语句进行遍历整数
for ( i = 0; i < n; i++)
{
    int num;    //当前的数
    scanf("%d",&num);   //输入当前整数
    if (i==0||num<min)
    {
    min=num;
    }
 }
 printf("%d\n",min);
}
 return 0;
}