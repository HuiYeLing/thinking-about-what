#include<bits/stdc++.h>
using namespace std;
int main() {
    // ��ȡ�����Ĵ���
    int n;
    cin >> n;
    // ����һ����������lights����ʾÿյ�Ƶ�״̬����ʼ״̬���ǹأ�false��
    // ����Ĵ�С��Ϊ2000005����Ϊ��Ŀ�и��������ֵ��2000000
    vector<bool> lights(2000005, false);
    // ��ÿ���������д���
    while (n--) {
        // ��ȡa��t��ֵ
        double a;
        int t;
        cin >> a >> t;

        // �Ա��Ϊ floor(i * a) �ĵ��л�״̬
        // i�ķ�Χ�Ǵ�1��t
        for (int i = 1; i <= t; i++) {
            // ����Ƶı��
            int index = floor(i * a);

            // �л��Ƶ�״̬
            // ������ǿ��ģ��ͱ�Ϊ�صģ�������ǹصģ��ͱ�Ϊ����
            lights[index] = !lights[index];
        }
    }
    // �ҵ�Ψһ���ŵĵ�
    // ����lights���飬�ҵ�Ψһһ��Ϊ�棨���ŵģ���Ԫ�أ�Ȼ�������������
    for (int i = 1; i < lights.size(); i++) {
        if (lights[i]) {
            cout << i << endl;
            break;
        }
    }
    return 0;
}