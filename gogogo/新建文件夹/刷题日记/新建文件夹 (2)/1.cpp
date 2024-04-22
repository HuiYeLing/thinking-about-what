#include<bits/stdc++.h>
using namespace std;

// 定义地毯的结构体，包括左下角的坐标（a，b）以及在x轴和y轴方向的长度（g，k）
struct Carpet {
    long long int a, b, g, k;
} carpets[10005];

int main() {
    long long int n, x, y;
    cin >> n; // 输入地毯的数量
    for (int i = 1; i <= n; i++) {
        // 输入每张地毯的信息
        cin >> carpets[i].a >> carpets[i].b >> carpets[i].g >> carpets[i].k;
    }
    cin >> x >> y; // 输入要查询的点的坐标
    for (int i = n; i >= 1; i--) {
        // 从最后一张地毯开始，检查每张地毯是否覆盖了指定的点
        if (x >= carpets[i].a && x <= carpets[i].a + carpets[i].g && y >= carpets[i].b && y <= carpets[i].b + carpets[i].k) {
            cout << i; // 如果找到了覆盖该点的地毯，输出其编号并结束程序
            return 0;
        }
    }
    cout << -1; // 如果没有找到覆盖该点的地毯，输出-1
    return 0;
}