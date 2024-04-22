#include <stdio.h>  
  
int main() {  
    int m, n, x, index,i;  
    scanf("%d", &m);  //输入测试组的数量
    while (m--) {  //循环输出组数
        scanf("%d", &n);  
        int a[n];  
        for (i = 0; i < n; i++) {  
            scanf("%d", &a[i]);  //循环输入数组数字
        }  
        scanf("%d", &x);  //输入x
        for (i = 0; i < n; i++) {  //遍历数组查找
            if (a[i] == x) {  
                index = i;  
                printf("%d\n", index);  //查找到输出下标
                break;  
            }  
        }  
        if (i == n) {  
            printf("Not Found\n");  
        }  
    }  
    return 0;  
}