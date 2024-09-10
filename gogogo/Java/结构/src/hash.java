import java.util.ArrayList;
import java.util.List;
class Pair {
    public int key;
    public String val;

    public Pair(int key, String val) {
        this.key = key;
        this.val = val;
    }
}
class ArrayHashMap{
    private List<Pair> buckets;//桶

    public ArrayHashMap(){
        buckets = new ArrayList<>();
        //初始化桶,桶的大小为10
        for(int i = 0; i < 10; i++){
            buckets.add(null);//初始化桶里面的元素为null
        }
    }
    //hash函数
    private int hashFunc(int key){
        int index = key % 10;//取余
        return index;
    }
    //查找操作
    public String get(int key){
        int index = hashFunc(key);//计算key的hash值
        Pair pair = buckets.get(index);//从桶中取出pair
        if(pair == null){//如果pair为空
            return null;//返回null
        }
        return pair.val;//返回pair的val
        
    }
    //添加操作
    public void put(int key,String val){
        Pair pair = new Pair(key,val);//创建一个pair
        int index = hashFunc(key);//计算key的hash值
        buckets.set(index, pair);//将pair放入桶中
    }

    //删除操作
    public void remove(int key){
        int index = hashFunc(key);//计算key的hash值
        buckets.set(index, null);//将桶中的pair置为null
    }
    //获取键值对
    public List<Pair> pairSet(){
        List<Pair> pairList = new ArrayList<>();//创建一个pairList
        for(Pair pair : buckets){//遍历桶
            if(pair != null){//如果pair不为空
                pairList.add(pair);//将pair加入pairList
            }
        }
        return pairList;//返回pairList   
    }

    //获取所有值
    public List<String> valueSet(){
        List<String> valueSet = new ArrayList<>();//创建一个valueSet
        for(Pair pair : buckets){//遍历桶
            if(pair != null){//如果pair不为空
                valueSet.add(pair.val);//将pair的val加入valueSet
            }
        }
        return valueSet;//返回valueSet
    }
    //打印哈希表
    public void print(){
        for(Pair kv : pairSet()){//遍历pairSet
            System.out.println(kv.key + " -> " + kv.val);//打印键值对
        }
    }
}