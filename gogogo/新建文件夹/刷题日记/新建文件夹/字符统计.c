#include<stdio.h>
#include<string.h>
int main()
{
    int zm=0,sz=0,kg=0,qt=0,i;
    char chr[100005];
    gets(chr);
    for ( i = 0; i <strlen(chr); i++)
    {
        if ((chr[i]>='A'&&chr[i]<='Z')||(chr[i]>='a'&&chr[i]<='Z'))
        {
        zm++;
        }
        if (chr[i]>='0'&&chr[i]<='9')
        {
            sz++;
        }
        if (chr[i]==' ')
        {
            kg++;
        }
        if (zm+sz+kg!=strlen(chr))
        {
            qt=strlen(chr)-zm-sz-kg;
        }
        
    }
    printf("%d %d %d %d",zm,sz,kg,qt);
    return 0;
}