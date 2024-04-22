#include <stdio.h>  
  
int main() {  
    int num, i, flag = 0;  
    scanf("%d", &num);  
  
    for (i = 2; i <= num / 2; i++) {  
        if (num % i == 0) {  
            flag = 1;  
            break;  
        }  
    }  
    if (flag == 0)  
        printf("%d是素数", num);  
    else  
        printf("%d不是素数", num);  
  
    return 0;  
}