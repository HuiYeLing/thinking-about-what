//动态规划
class Solution {
public:
    int fib(int n) {
        if (n==0)
        {
            return 0;
        }
        if (n==1)
        {
            return 1;
        }
        int dp[50];
        dp[0]=1;
        dp[1]=1;
        for (int i = 2; i <=n; i++)
        {
            dp[i]=dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
};

