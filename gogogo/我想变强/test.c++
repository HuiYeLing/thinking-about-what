#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e5+5;
const int inf = 0x3f3f3f3f;
int dp[maxn][3], sum[maxn][3];
char s[maxn];
int main() {
    int n, q;
    scanf("%d%d", &n, &q);
    scanf("%s", s + 1);
    memset(dp, inf, sizeof(dp));
    dp[0][0] = 0;
    for(int i = 1; i <= n; i++) {
        for(int j = 0; j < 3; j++) sum[i][j] = sum[i-1][j];
        if(s[i] == 'r') sum[i][0]++;
        else if(s[i] == 'e') sum[i][1]++;
        else sum[i][2]++;
        for(int j = 0; j < 3; j++) {
            dp[i][j] = dp[i-1][j];
            if(j) dp[i][j] = min(dp[i][j], dp[i-1][j-1] + sum[i][j-1]);
        }
    }
    while(q--) {
        int l, r;
        scanf("%d%d", &l, &r);
        printf("%d\n", dp[r][2] - dp[l-1][2] + sum[l-1][2]);
    }
    return 0;
}