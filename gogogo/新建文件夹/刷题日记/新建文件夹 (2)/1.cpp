#include<bits/stdc++.h>
using namespace std;

// �����̺�Ľṹ�壬�������½ǵ����꣨a��b���Լ���x���y�᷽��ĳ��ȣ�g��k��
struct Carpet {
    long long int a, b, g, k;
} carpets[10005];

int main() {
    long long int n, x, y;
    cin >> n; // �����̺������
    for (int i = 1; i <= n; i++) {
        // ����ÿ�ŵ�̺����Ϣ
        cin >> carpets[i].a >> carpets[i].b >> carpets[i].g >> carpets[i].k;
    }
    cin >> x >> y; // ����Ҫ��ѯ�ĵ������
    for (int i = n; i >= 1; i--) {
        // �����һ�ŵ�̺��ʼ�����ÿ�ŵ�̺�Ƿ񸲸���ָ���ĵ�
        if (x >= carpets[i].a && x <= carpets[i].a + carpets[i].g && y >= carpets[i].b && y <= carpets[i].b + carpets[i].k) {
            cout << i; // ����ҵ��˸��Ǹõ�ĵ�̺��������Ų���������
            return 0;
        }
    }
    cout << -1; // ���û���ҵ����Ǹõ�ĵ�̺�����-1
    return 0;
}