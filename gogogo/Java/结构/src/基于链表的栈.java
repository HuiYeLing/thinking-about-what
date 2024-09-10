//基于链表实现栈
class ListkedListStack{
        private ListNode stackPeek;//栈顶指针
        private int stkSize=0;//栈的大小

    public ListkedListStack(){
        stackPeek=null;
    }
    //获取栈的长度
    public int size(){
        return stkSize;
    }
    //判断栈是否为空
    public boolean isEmpty(){
        return stkSize==0;
    }
    //入栈
    public void push(int num){
        ListNode node = new ListNode(num);
        node.next=stackPeek;
        stackPeek=node;
        stkSize++;
    }
    //出栈
    public int pop(){
        int num = peek();//获取栈顶元素
        stackPeek = stackPeek.next;//栈顶指针指向下一个元素
        stkSize--;//栈的大小减一
        return num;//返回栈顶元素
    }
    //获取栈顶元素
    public int peek(){
        if(isEmpty())
            throw new RuntimeException();
        return stackPeek.val;
    }
    //将List转化为Array并返回
    public int [] toArray(){
        ListNode node = stackPeek;
        int [] res = new int[size()];
        for(int i=res.length-1;i>=0;i--){
            res[i]=node.val;
            node=node.next;
        }
        return res;
    }
}
