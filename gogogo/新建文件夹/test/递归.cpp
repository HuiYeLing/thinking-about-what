#include<iostream>
using namespace std;

int f(int n)
{
    int res=1;
    if (n==1)
    {
        res=1;
    }
    else
    {
        res=n*f(n-1); //�ݹ���ã����n�Ľ׳�
    }
    return res;
}

int main()
{
    int x;
    cin >> x;
    cout << f(x);
    return 0;
}