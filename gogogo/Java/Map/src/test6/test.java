package test6;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
public class test {
    public static void main(String[] args) {
        List<School> list=new ArrayList<School>();
        School s1=new School("1","绍职院","绍兴");
        School s2=new School("2","宁职院","宁波");   
        School s3=new School("3","温职院","温州");
        list.add(s1);
        list.add(s2);
        list.add(s3);
        Collections.sort(list,new MyComparator());
        System.out.println(list);
    }
}
