#include<iostream>
using namespace std;
int main()
{
    long long int a[60]={0};
    a[1]=1;
    a[2]=1;
    for (int  i = 3; i <=50; i++)
    {
        a[i]=a[i-1]+a[i-2];
    }
    for (int  i = 0; i <= 50; i++)
    {
        cout<< i <<":" << a[i] << endl; 
    }
    
    return 0;
}