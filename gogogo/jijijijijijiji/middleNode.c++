#include <iostream>
using namespace std;

// 定义链表节点结构体
struct ListNode {
    int val;  // 节点值
    ListNode *next;  // 指向下一个节点的指针
    ListNode() : val(0), next(nullptr) {}  // 默认构造函数，初始化节点值为0，next指针为nullptr
    ListNode(int x) : val(x), next(nullptr) {}  // 构造函数，初始化节点值为x，next指针为nullptr
    ListNode(int x, ListNode *next) : val(x), next(next) {}  // 构造函数，初始化节点值为x，next指针为传入的next
};

// 定义解决方案类
class Solution {
public:
    // 定义公共方法，找到链表的中间节点
    ListNode* middleNode(ListNode* head) 
    {
        int length=0;
        ListNode* temp=head;  // 定义临时节点指针，指向头节点
        // 第一次遍历链表，计算链表长度
        while(temp!=nullptr)// 遍历链表，直到链表尾部
        {
            length++;
            temp=temp->next;
        }
        temp=head;  // 重置临时节点指针
        // 第二次遍历链表，找到中间节点
        for(int i=0;i<length/2;i++)
        {
            temp=temp->next;
        }
        return temp;  // 返回中间节点
    }
};

int main() {
    // 创建链表 1->2->3->4->5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    // 创建解决方案类实例
    Solution solution;

    // 调用 middleNode 方法
    ListNode* middle = solution.middleNode(head);

    // 打印中间节点的值
    cout << "Middle node value: " << middle->val << endl;

    return 0;
}