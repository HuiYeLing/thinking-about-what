#include<stdio.h>  
  
int main()  
{  
    int i, p, n;  
    char a[100], temp;  
    scanf("%d", &n);  
    getchar();  
    for (i = 0; i < n; i++)  
        scanf("%c", &a[i]);  
    getchar();  
    for (i = 0; i < n-1; i++) {  
        p = i;  
        for (int j = i+1; j < n; j++) {  
            if (a[j] < a[p])  
                p = j;  
        }  
        temp = a[p];  
        a[p] = a[i];  
        a[i] = temp;  
    }  
    for (i = 0; i < n; i++)  
        printf("%c", a[i]);  
    return 0;  
}
