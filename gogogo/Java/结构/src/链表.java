import java.util.List;

public class 链表 {
    class ListNode {
        int val;// 节点的值
        ListNode next; // 下一个节点的指针
        ListNode(int x) {
            val = x;
        }// 节点的构造函数
    }
    //初始化链表1->3->2->5->4
    //初始化各节点
    ListNode n0 = new ListNode(1);
    ListNode n1 = new ListNode(3);
    ListNode n2 = new ListNode(2);
    ListNode n3 = new ListNode(5);
    ListNode n4 = new ListNode(4);
    //连接各节点
    public 链表() {
        n0.next = n1;
        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
    }
    //插入节点
    void insert(ListNode n0, ListNode P)
    {
        ListNode n1 =n0.next;
        P.next = n1;
        n0.next = P;
        //在链表节点n0后插入节点P
    }
    //删除节点
    //删除节点n0后的节点
    void remove(ListNode n0){
        if (n0.next == null) 
            return;
        ListNode P = n0.next;
        ListNode n1 = P.next;
        n0.next = n1;
    }
    //访问节点
    //访问链表中的第index个节点
    ListNode access(ListNode head,int index){
        for(int i=0;i<index;i++){
            if (head==null) 
                return null;
            head = head.next;
        }
        return head;
    }
    //查找节点
    int find(ListNode head,int target){
        int index=0;
        while (head!=null) {
            if (head.val==target) {
                return index;
            }
            head = head.next;
            index++;
        }
        return -1;
    }
}
