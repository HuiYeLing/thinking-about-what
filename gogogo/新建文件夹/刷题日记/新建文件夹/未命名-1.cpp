#include<bits/stdc++.h>
using namespace std;
void main()
{
  char x;
  int i,sum=0;
  scanf("%s",&x);
  for ( i = 0; i < x.size(); i++)
  {
    if ('0'<=x && x<='9')
    {
      sum++;
    }
    
  }
  printf("%d",sum);
  return 0;  
}
