#include <stdio.h> // 引入标准输入输出库  
  
int main() { // 主函数入口  
    int m; // 测试数组的个数  
    scanf("%d", &m); // 读入测试数组的个数  
  
    while (m--) { // 对每个测试数组进行遍历  
        int n; // 整数个数  
        scanf("%d", &n); // 读入整数个数  
  
        int min = 0; // 记录当前最小值，初始化为0  
  
        for (int i = 0; i < n; i++) { // 遍历所有整数  
            int num; // 当前整数  
            scanf("%d", &num); // 读入当前整数  
  
            if (i == 0 || num < min) { // 如果当前整数比当前最小值小，更新当前最小值  
                min = num;  
            }  
        }  
  
        printf("%d\n", min); // 输出最小值  
    }  
  
    return 0; // 主函数返回0，表示程序正常结束  
}