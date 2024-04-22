#include<bits/stdc++.h>
using namespace std;
int main() {
    // 读取操作的次数
    int n;
    cin >> n;
    // 创建一个布尔数组lights，表示每盏灯的状态，初始状态都是关（false）
    // 数组的大小设为2000005，因为题目中给出的最大值是2000000
    vector<bool> lights(2000005, false);
    // 对每个操作进行处理
    while (n--) {
        // 读取a和t的值
        double a;
        int t;
        cin >> a >> t;

        // 对编号为 floor(i * a) 的灯切换状态
        // i的范围是从1到t
        for (int i = 1; i <= t; i++) {
            // 计算灯的编号
            int index = floor(i * a);

            // 切换灯的状态
            // 如果灯是开的，就变为关的；如果灯是关的，就变为开的
            lights[index] = !lights[index];
        }
    }
    // 找到唯一开着的灯
    // 遍历lights数组，找到唯一一个为真（开着的）的元素，然后输出它的索引
    for (int i = 1; i < lights.size(); i++) {
        if (lights[i]) {
            cout << i << endl;
            break;
        }
    }
    return 0;
}