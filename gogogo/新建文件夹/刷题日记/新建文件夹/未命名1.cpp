#include <stdio.h>  
  
int main() {  
    int i,n;  
    double s = 0, fz = 1, fm = 2, qfm = 0;  
    scanf("%d", &n);  
    for ( i = 1; i <= n; i++) {  
        s += fz / fm;  
        qfm = fm;  
        fz = fz + fm;  
        fm = fz + qfm;  
    }  
    printf("%.3f\n", s);  
    return 0;  
}
