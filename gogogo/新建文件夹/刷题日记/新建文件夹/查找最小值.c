#include<stdio.h>  
  
void sort(int *p,int m);  
  
int main()  
{  
 int n, i, j, a[1005], b[1005];  
 while (scanf("%d", &n), n != 0)  
 {  
 for (i = 0; i < n; i++)  
 {  
 scanf("%d", &a[i]);  
 }  
 for (i = 0; i < n; i++)  
 {  
 scanf("%d", &b[i]);  
 }  
 sort(a, n);  
 sort(b, n);  
 i = 0;  
 j = 0;  
 while (i < n && j < n)  
 {  
 if (a[i] > b[j])  
 {  
 i++;  
 j++;  
 }  
 else  
 i++;  
 }  
 if (j == n)  
 printf("YES\n");  
 else if (i < n)  
 printf("NO\n");  
 else  
 printf("YES\n"); // 当n是偶数时，a和b都有n/2个元素，所以打印YES  
 }  
   
 return 0;  
}  
  
void sort(int *p, int m)  
{  
 int i, j, temp;  
 for (i = 1; i < m; i++)  
 {  
 for (j = 0; j < m-i; j++)  
 {  
 if (p[j] > p[j+1])  
 {  
 temp = p[j];  
 p[j] = p[j+1];  
 p[j+1] = temp;  
 }  
 }  
 }  
}