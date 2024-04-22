#include<stdio.h>

void asc(char ch);
void asc(char ch)
{
   printf("%d",ch);
}

int main()
{
   char a;
   scanf("%c",&a);
   asc(a);
   return 0;
}