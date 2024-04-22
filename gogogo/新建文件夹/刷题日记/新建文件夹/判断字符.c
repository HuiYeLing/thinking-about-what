#include<stdio.h>  
  
int main()  
{  
    char x;  
    scanf("%c",&x);  
    if((x>='a' && x<='z')||(x>='A' && x<='Z'))  
    printf("%d\n",x);  
    return 0;  
}

