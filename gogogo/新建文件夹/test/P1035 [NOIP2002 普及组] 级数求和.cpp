#include<bits/stdc++.h>
using namespace std;

int main() {
    int n = 0; // ��ʼ��nΪ0��n��ʾ����������
    int k; // k��ʾĿ���
    double s = 0; // ��ʼ��sΪ0��s��ʾ��ǰ�ĺ�
    cin >> k; // ����Ŀ���k

    // ʹ������ѭ����ֱ���ҵ�����������n
    while (true) {
        n++; // ÿ��ѭ����n����1
        s += 1.0 / n; // ��1/n�ӵ�s�ϣ����㼶���ĺ�

        // �����ǰ�ĺ�s����Ŀ���k����ô���n������ѭ��
        if (s > k) {
            cout << n;
            break;
        }
    }
    return 0; // ������������
}