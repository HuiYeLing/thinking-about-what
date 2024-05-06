
public class ListNode {
int val;
ListNode next;
ListNode() {}
ListNode(int val) { this.val = val; }
ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
class Solution {
    public ListNode middleNode(ListNode head) {
        if (head == null) {
            return null;  // 如果链表为空，返回 null
        }
        int length = 0;
        ListNode temp = head;
        while (temp != null) {
            length++;
            temp = temp.next;
        }
        int count = 0;
        temp = head;
        while (count < length / 2) {
            count++;
            temp = temp.next;
        }
        return temp;
    }
}