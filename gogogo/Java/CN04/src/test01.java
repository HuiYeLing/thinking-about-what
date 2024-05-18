import java.util.ArrayList;
import java.util.List;

public class test01 {
    public static void main(String[] args) {
        //要求集合中只能添加某类型数据

        List<Double> list=new ArrayList<Double>();
            // list.add("aa");
            // list.add("bb");
            // list.add("cc");
            // list.add(1);
            list.add(1.2);
            // list.add("aa");
            // list.add("3.14");
        for (int i = 0; i < list.size(); i++) {
            double o = list.get(i);//有了泛型之后，返回值为double
            System.out.println(o);
        }
        
    }
}
