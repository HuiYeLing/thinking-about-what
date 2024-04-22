#include<bits/stdc++.h>
using namespace std;

int main() {
    int n = 0; // 初始化n为0，n表示级数的项数
    int k; // k表示目标和
    double s = 0; // 初始化s为0，s表示当前的和
    cin >> k; // 读入目标和k

    // 使用无限循环，直到找到满足条件的n
    while (true) {
        n++; // 每次循环，n增加1
        s += 1.0 / n; // 将1/n加到s上，计算级数的和

        // 如果当前的和s大于目标和k，那么输出n并结束循环
        if (s > k) {
            cout << n;
            break;
        }
    }
    return 0; // 程序正常结束
}