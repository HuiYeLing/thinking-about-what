#include<stdio.h>

void countdigit(number,digit);
void countdigit(number,digit)
{
    int a[6];
    int *p=a;
    int num=0;
    for (int  i = 0; i < 6; i++)
    {
        *p=i;
        if (*p==digit)
        {
            num++;
        }
        
    }
    return num;
}

int main() {  
    int x, y;  
    scanf("%d%d", &x, &y);  
    countdigit(x, y); 
    return 0;  
}