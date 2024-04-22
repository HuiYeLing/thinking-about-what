#include <stdio.h>
#include <stdlib.h>

// ��������ڵ�
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// �����½ڵ�
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if(newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(0);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// ��ӽڵ㵽�����ĩβ
void appendNode(Node** head, int data) {
    Node* newNode = createNode(data);
    if(*head == NULL) {
        *head = newNode;
        return;
    }
    Node* temp = *head;
    while(temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// ��ӡ����
void printList(Node* head) {
    Node* temp = head;
    while(temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    Node* head = NULL;
    appendNode(&head, 1);
    appendNode(&head, 2);
    appendNode(&head, 3);
    printList(head);
    return 0;
}