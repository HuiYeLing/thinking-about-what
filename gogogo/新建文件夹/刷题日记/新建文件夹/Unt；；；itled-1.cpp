#include <iostream>
#include <cmath>
using namespace std;
bool prime(int x)
{
  if(x==2) return true;
  for(int i=2;i<=sqrt((float) x);i++)
  //如果为i<t,输入16输出为2*2*4
  //因为，sqrt(4)等于2时就退出循环了，于是程序将4也当作了素数
  {
    if(x%i==0)
    return false;
        
  }
   return true;
} 
void f(int x)
{ int tag=2,flag=0;
  for(;;)
 {
   if(prime(x))
    {
    if(flag>0) cout<<' ';
    cout<<x<<endl;
    return;//跳到无限循环的唯一地方
    }
   if(x%tag==0)
    {
     if(flag>0) cout<<' ';         
     cout<<tag;
     x/=tag;
     flag++;
    }
   else
   {   tag++;//没有这一句，输入65535进入死循环
 
       while(!prime(tag))
       tag++;
   }         
 }

} 
     

int main()
{int t;
while(cin>>t)
{
 if(!t) break;
 f(t);
             
            
}
  system("pause");
   return 0;
}