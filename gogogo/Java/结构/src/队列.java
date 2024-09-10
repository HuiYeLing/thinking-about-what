
class LinkedListQueue {
    private ListNode front,rear;//头节点front，尾节点rear
    private int queSize=0;//队列的大小

    public LinkedListQueue(){
        //初始化队列
        front = null;
        rear = null;
    }

    public int size(){
        //返回队列的大小
        return queSize;
    }

    public boolean isEmpty(){
        //判断队列是否为空
        return queSize==0;
    }

    //入队
    public void push(int num){
        //创建一个新的节点
        ListNode node = new ListNode(num);
        //如果队列为空 则头尾节点都指向新节点
        if (front==null){
            front = node;
            rear = node;}
            //否则尾节点指向新节点
        else{
            rear.next = node;
            rear = node;
        }
        queSize++;//队列大小加1
        }
    //出队
    public int pop(){
        int num = front.val;//获取队头元素
        //删除队头元素
        front = front.next;
        queSize--;
        return num;
    }
    //获取队头元素
    public int peek(){
        if (isEmpty())
            throw new RuntimeException();
        return front.val;//返回队头元素
        
    
}
    // 将链表转化为Array并返回
    public int[] toArray() {
    ListNode node = front;
    int[] res = new int[size()];
    // 遍历链表
    for (int i = 0; i < res.length; i++) {
        res[i] = node.val;
        node = node.next;
    }
    // 返回数组
    return res;
}

}

    
