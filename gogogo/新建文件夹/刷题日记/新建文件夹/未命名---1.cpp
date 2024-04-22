#include <stdio.h>  
#include <stdlib.h>  
  
// 比较函数，用于排序  
int cmp(const void *a, const void *b) {  
    return *(char *)b - *(char *)a;  
}  
  
// 删除数字函数  
void deleteDigits(int n, int k) {  
    char num[n + 1]; // 存储数字的字符数组  
    int len = n - k; // 删除k个数字后的新数字长度  
    for (int i = 0; i < n; i++) {  
        num[i] = '0' + (n % 10); // 将数字转换为字符并存储到数组中  
        n /= 10;  
    }  
    num[n] = '\0'; // 添加字符串结尾标志  
    qsort(num, len, sizeof(char), cmp); // 对数组进行排序  
    printf("新数字为：");  
    for (int i = 0; i < len; i++) {  
        printf("%c", num[i]); // 输出新数字  
    }  
    printf("\n");  
}  
  
int main() {  
    int n, k;  
    scanf("%d%d", &n, &k);  
    deleteDigits(n, k);  
    return 0;  
}
