package test6;

import java.util.Comparator;
public class MyComparator implements Comparator{
    @Override
    public int compare(Object o1, Object o2) {
        School s1=(School)o1;
        School s2=(School)o2;
        return s1.getId()-s2.getId();
    }
}
