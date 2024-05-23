import java.util.Comparator;
public class MyComparator implements Comparator{
    @Override
    public int compare(Object o1, Object o2) {
        Person s1 = (Person) o1;
        Person s2 = (Person) o2;
        return s1.getId()-s2.getId();
    }
}
