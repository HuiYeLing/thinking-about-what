#include<bits/stdc++.h>
using namespace std;

int main() {
    char c;
    cin >> c;
    int n = 3; // �߶�Ϊ3
    int m = 5; // �ױ߳���Ϊ5
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (j >= n - 1 - i && j <= n - 1 + i) {
                cout << c;
            } else {
                cout << " ";
            }
        }
        cout << "\n";
    }
    return 0;
}