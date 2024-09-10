class ArrayQueue{
    private int[] nums;
    private int front;
    private int queSize;

    public ArrayQueue(int capacity)
    {
        nums = new int[capacity];
        front = queSize = 0;
    }
    //获取队列容量
    public int capacity(){
        return nums.length;
    }
    //获取队列长度
    public int size(){
        return queSize;
    }
    //判断队列是否为空
    public boolean isEmpty(){
        return queSize==0;
    }
    //入队
    public void push(int num){ 
        if (queSize==nums.length){
           System.out.println("队列已满");
            return;
        } 
        //计算队尾指针，指向队尾索引+1
        //通过取余操作实现rear越过数组尾部后重新指向数组头部
        int rear = (front+queSize)%capacity();
        //将元素num放入队尾
        nums[rear] = num;
        queSize++;//队列大小加1

    }
    //出队
    public int pop(){
        int num = peek();
        front = (front+1)%capacity();
        queSize--;
        return num;
    }
    //获取队头元素
    public int peek(){
        if (isEmpty())//如果队列为空，抛出异常
            throw new RuntimeException();
        return nums[front];//返回队头元素
    }
    // 将数组转化为Array并返回
    public int [] toArray(){
        
        int[] res = new int[size()];//创建一个数组
        for (int i = 0; i < res.length; i++) {
            res[i] = nums[(front+i)%capacity()];//通过取模运算来计算当前元素在底层数组 nums 中的位置，确保索引不会越界
        }
        return res;
    }
}