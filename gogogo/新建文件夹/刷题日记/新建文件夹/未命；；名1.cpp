#include <stdio.h>
#include <stdlib.h>

#define MAXN 1000

int stack[MAXN], top;
int target[MAXN];

int main() {
    int n, i, j;
    while (scanf("%d", &n) == 1 && n) {
        while (scanf("%d", &target[1]) == 1 && target[1]) {
            for (i = 2; i <= n; i++)
                scanf("%d", &target[i]);
            top = 0;
            j = 1;
            for (i = 1; i <= n; i++) {
                stack[++top] = i;
                while (top && stack[top] == target[j]) {
                    top--;
                    j++;
                }
            }
            if (top)
                printf("No\n");
            else
                printf("Yes\n");
        }
        printf("\n");
    }
    return 0;
}
