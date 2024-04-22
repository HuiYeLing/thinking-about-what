#include <bits/stdc++.h>
#define IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
int n, c;
int main()
{
    IO;
    int l,i; cin >> l;
    while (l --) {
        int a[30] = {0};
        c = 0;
        string s; 
        cin >> n >> s;
        int len = s.size();
        for ( i = 0; i < len; i++) {
            a[s[i] - 'A']++;
        }
        if (a[0] >= 1 && a[2] / 2 >= 1 && a[4] >= 1 && a[19] >= 1 && a[15] >= 1) {
            cout << min(min(a[0], a[2]/2), min(min(a[4], a[19]), a[15])) << "\n";
        } else {
            cout << 0 << "\n";
        }
    }
    return 0;
}