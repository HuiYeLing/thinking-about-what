#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> matrix(n);
    for (int i = 0; i < n; ++i) {
        cin >> matrix[i];
    }

    for (int size = 1; size <= n; ++size) {
        int count = 0;
        for (int i = 0; i <= n - size; ++i) {
            for (int j = 0; j <= n - size; ++j) {
                int zeros = 0, ones = 0;
                for (int x = i; x < i + size; ++x) {
                    for (int y = j; y < j + size; ++y) {
                        if (matrix[x][y] == '0') {
                            ++zeros;
                        } else {
                            ++ones;
                        }
                    }
                }
                if (zeros == ones) {
                    ++count;
                }
            }
        }
        cout << count << endl;
    }

    return 0;
}