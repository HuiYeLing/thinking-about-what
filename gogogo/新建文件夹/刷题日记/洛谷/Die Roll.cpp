// Yakko、Wakko 和 Dot 是世界著名的动画狂，他们决定不再出演动画片，并请假去旅行一下。Yakko梦想着去宾夕法尼亚州，他的祖国和他祖先的祖国。Wakko想到了塔斯马尼亚，它的海滩，阳光和大海。多特选择特兰西瓦尼亚作为最神秘、最不可预测的地方。

// 但令他们非常遗憾的是，假期变得非常短暂，因此参观上述三个地方之一就足够了。这就是为什么最聪明的 Yakko 想出了一个真正天才的想法：让三个人中的每一个掷出一个普通的六面骰子，得分最高的人将成为赢家，并将另外两个人带到他/她梦想的地方。

// Yakko 掷了一个骰子并得到了 Y 点，Wakko — W 点。轮到多特了。但她并不着急。多特想知道她访问特兰西瓦尼亚的机会有多大。

// 众所周知，Yakko 和 Wakko 是真正的绅士，这就是为什么如果他们与 Dot 的积分相同，他们会让 Dot 获胜。

// 输入
// 输入文件的唯一一行包含两个自然数 Y 和 W，即 Yakko 和 Wakko 掷骰子的结果。

// 输出
// 以“A/B”格式的不可约分数形式输出所需的概率，其中 A — 分子，B — 分母。如果所需概率等于零，则输出 ?0/1?。如果所需概率等于 1，则输出 ?1/1?。

// 例子
// 输入复制
// 4 2
// 输出复制
// 1/2
// 注意
// 多特将前往特兰西瓦尼亚，如果她幸运地掷出 4、5 或 6 分。

#include<bits/stdc++.h>
using namespace std;

// 计算最大公约数的函数
int gcd(int a, int b) {
    // 如果b为0，返回a，否则递归调用gcd函数
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    int Y, W;
    // 读取Yakko和Wakko掷出的点数
    cin >> Y >> W;
    // 计算最大点数
    int max_point = max(Y, W);
    // 计算掷出最大点数或更大点数的可能性
    int numerator = 6 - max_point + 1;
    // 总的可能性是6
    int denominator = 6;
    // 计算最大公约数
    int g = gcd(numerator, denominator);
    // 输出化简后的概率
    cout << numerator / g << "/" << denominator / g << endl;
    return 0;
}