#include <stdio.h>  
int main() {  
    int n,i;  
    double s;
    scanf("%d",&n);  
     for (i = 1; i <= n; i++) {  
        s += 1.0/ ( 2.0 * i);  
    }  
    printf("%.2f",s);  
    return 0;  
}
