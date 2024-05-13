#include<bits/stdc++.h>
using namespace std;
int main()
{
        long long int a[30][30]={0};  // 初始化棋盘
        long long int n,m;  // 棋盘的大小
        cin >> n >> m;
        long int x,y;  // 阻碍的位置
        cin >> x >> y; 
        for (int  i = 0; i <=n; i++)
        {
            for (int j = 0; j<=m; j++) 
            {
                a[i][j]=1;  // 将棋盘所有位置设为可走
            }
            
        }
        a[x][y]=0;  // 将阻碍位置设为不可走
        // 将阻碍位置周围的位置也设为不可走
        if (x+2<=n && y-1>=0)
        {
            a[x+2][y-1]=0;
        }
        if (x+2<=n && y+1<=m)
        {
            a[x+2][y+1]=0;
        }
        if (x+1<=n && y+2<=m)
        {
            a[x+1][y+2]=0;
        }
        if (x-1>=0 && y+2<=m)
        {
            a[x-1][y+2]=0;
        }
        if (x-2>=0 && y+1<=m)
        {
            a[x-2][y+1]=0;
        }
        if (x-2>=0 && y-1>=0)
        {
            a[x-2][y-1]=0;
        }
        if (x-1>=0 && y-2>=0)
        {
            a[x-1][y-2]=0;
        }
        if (x+1<=n && y-2>=0)
        {
            a[x+1][y-2]=0;
        }
        // 计算每个位置的走法数量
        for (int  i = 0; i <=n; i++)
        {
                for ( int j = 0; j <=m; j++)
                {
                     if (i==0 && j==0)  // 左上角位置跳过
                     {
                         continue; 
                     }
                     if (a[i][j]==0)  // 不可走的位置跳过
                     {
                        continue;
                     }
                     if (i==0)  // 第一行的位置只能从左边来
                     {
                       a[i][j]=a[i][j-1];
                     }
                     else if (j==0)  // 第一列的位置只能从上边来
                     {
                        a[i][j]=a[i-1][j];
                     }
                     else  // 其他位置可以从左边或上边来
                        {
                         a[i][j]=a[i-1][j]+a[i][j-1];
                        }
                }
                
        }
        cout << a[n][m];  // 输出右下角的走法数量
}