#include<iostream>
using namespace std;

int f(int n)
{
    int res;
    if (n==1 || n==2)
    {
        res=1;
    }
    else
    {
        res=f(n-1)+f(n-2);
    }
    return res;
}

int main()
{   
    long long int a;
    cin>>a;
    for (int  i = 1; i <= 50; i++)
    {
        cout<<i<<":"<<f(i)<<endl;
    }
    
    return 0;
}