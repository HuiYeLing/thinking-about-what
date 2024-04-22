#include<stdio.h> // 引入标准输入输出库，以使用printf等函数  
  
int main(void) // 主函数，程序执行的入口点  
{  
    int a[]={1,456,6767,33,55,78,99,0,78}; // 定义一个整数数组，并初始化  
    int min,max; // 定义两个整数变量，用于存储最小值和最大值  
    minmax(a,sizeof(a)/sizeof(a[0]),&min,&max); // 调用minmax函数，传入数组，数组长度和两个整数的地址  
    printf("min=%d,max=%d\n",min,max); // 打印找到的最小值和最大值  
  
    return 0; // 主函数返回0，表示程序正常结束  
}  
  
void minmax(int a[],int len,int *min,int *max) // 定义一个函数，接收一个整数数组，数组的长度，和两个整数的指针  
{  
    int i; // 定义一个整数，用于循环控制  
    *min= *max=a[0]; // 将数组的第一个元素设为初始的最小值和最大值  
    for ( i = 1; i < len; i++) // 从数组的第二个元素开始，遍历数组  
    {  
        if (a[i]<*min) // 如果当前元素小于当前最小值  
        {  
           *min=a[i]; // 则更新最小值  
        }  
        if (a[i]>*max) // 如果当前元素大于当前最大值  
        {  
            *max=a[i]; // 则更新最大值  
        }  
    }  
}