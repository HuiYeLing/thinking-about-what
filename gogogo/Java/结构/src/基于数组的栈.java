import java.util.ArrayList;

class Arraystack{
    private ArrayList<Integer> stack;

    public Arraystack(){
        //初始化列表（动态数组）
        stack = new ArrayList<>();
    }
    //获取栈的长度
    public int size(){
        return stack.size();
    }
    //判断栈是否为空
    public boolean isEmpty(){
        return size() == 0;
    }

    //入栈
    public void push(int num){
        stack.add(num);
    }

    //出栈
    public int pop(){
        if(isEmpty())//判断栈是否为空
            throw new RuntimeException();//抛出异常
        return stack.remove(size()-1);//返回栈顶元素
    }

    //获取栈顶元素
    public int peek(){
        if(isEmpty())//判断栈是否为空
            throw new RuntimeException();//抛出异常
        return stack.get(size()-1);//返回栈顶元素
    }

    //将List转化为Array并返回
    public Object[] toArray(){
        return stack.toArray();//将列表转化为数组并返回
    }
}