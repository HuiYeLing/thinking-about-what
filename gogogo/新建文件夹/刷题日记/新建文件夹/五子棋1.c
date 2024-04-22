#include <stdio.h>  
#include <stdlib.h>  
#include <stdbool.h>  
  
#define SIZE 15  
  
bool board[SIZE][SIZE] = {false};  
  
void printBoard() {  
    for (int i = 0; i < SIZE; i++) {  
        for (int j = 0; j < SIZE; j++) {  
            if (board[i][j]) {  
                printf("X ");  
            } else {  
                printf(". ");  
            }  
        }  
        printf("\n");  
    }  
}  
  
bool checkWin(int x, int y) {  
    return (board[x][y] &&  
            board[x - 1][y] &&  
            board[x + 1][y] &&  
            board[x][y - 1] &&  
            board[x][y + 1]);  
}  
  
bool isEmpty(int x, int y) {  
    return !board[x][y];  
}  
  
int main() {  
    int x, y;  
    bool gameEnded = false;  
    printf("��������Ϸ\n");  
    while (!gameEnded) {  
        printBoard();  
        printf("���X�����������λ�� (row column): ");  
        scanf("%d %d", &x, &y);  
        if (checkWin(x, y)) {  
            printf("���XӮ��!\n");  
            gameEnded = true;  
        } else if (!isEmpty(x, y)) {  
            printf("��λ���ѱ�ռ�ã�����������.\n");  
        } else {  
            board[x][y] = true;  
        }  
    }  
    return 0;  
}